import time

from logger import logger

from automation.action import (
    wait_for_template_gone,
    wait_for_any_template,
    wait_for_template,
)
from automation.mouse import click_window
from automation.screenshot import screenshot_canvas
from automation.vision import find_template


def run_battle():
    """
    执行战斗流程。

    流程：

    1. 等待 MAIN_QUEST 消失，确认进入战斗
    2. 检测 start_fight / skip / next
    3. 如果检测到 next：
       - 等待升级窗口加载
       - 输出升级窗口模板匹配信息
       - 如果升级窗口出现，点击关闭
       - 等待升级窗口消失
       - 然后重新检测
    4. 如果确认没有升级窗口，点击 next
    5. next 点击后，战斗流程结束
    """

    logger.info("开始执行战斗流程")

    # ==================================
    # 模板
    # ==================================

    mainquest_template = (
        "templates/quest/mainquest/mainquest.png"
    )

    next_template = (
        "templates/quest/mainquest/next.png"
    )

    level_up_template = (
        "templates/quest/mainquest/mine_level_up.png"
    )

    battle_templates = [
        (
            "start_fight",
            "templates/quest/mainquest/start_fight.png",
        ),
        (
            "skip",
            "templates/quest/mainquest/skip.png",
        ),
        (
            "next",
            next_template,
        ),
    ]

    # ==================================
    # 1. 等待 MAIN_QUEST 消失
    # ==================================

    logger.info("等待 MAIN_QUEST 消失")

    wait_for_template_gone(
        mainquest_template,
    )

    logger.info("MAIN_QUEST 已消失，确认进入战斗")

    # ==================================
    # 2. 持续执行战斗
    # ==================================

    while True:

        name, score, location, size = wait_for_any_template(
            battle_templates,
            timeout=30.0,
        )

        logger.info(
            f"检测到：{name}，"
            f"匹配度：{score:.3f}"
        )

        # ==================================
        # 3. 普通战斗按钮
        # ==================================

        if name != "next":

            x, y = location
            width, height = size

            click_window(
                x,
                y,
                width,
                height,
            )

            logger.info(f"{name} 点击完成")

            continue

        # ==================================
        # 4. 检测到 next
        # ==================================

        logger.info(
            "检测到 next，等待升级窗口加载"
        )

        time.sleep(0.8)

        # ==================================
        # 5. 检查升级窗口
        # ==================================

        logger.info(
            f"开始检测升级窗口：{level_up_template}"
        )

        try:

            level_up_score, level_up_location, level_up_size = (
                wait_for_template(
                    level_up_template,
                    timeout=1.0,
                )
            )

            logger.info(
                f"升级窗口匹配成功："
                f"score={level_up_score:.3f}, "
                f"location={level_up_location}, "
                f"size={level_up_size}"
            )

            x, y = level_up_location
            width, height = level_up_size

            click_window(
                x,
                y,
                width,
                height,
            )

            logger.info("升级窗口点击完成")

            wait_for_template_gone(
                level_up_template,
                timeout=5.0,
            )

            logger.info(
                "升级窗口已关闭，重新检测"
            )

            continue


        except TimeoutError:

            logger.warning(

                "升级窗口匹配失败，开始输出诊断信息"

            )

            screenshot = screenshot_canvas()

            (

                level_up_found,

                level_up_score,

                level_up_location,

                level_up_size,

            ) = find_template(

                screenshot,

                level_up_template,

                threshold=0.8,

            )

            logger.warning(

                f"升级窗口匹配结果："

                f"found={level_up_found}, "

                f"score={level_up_score:.3f}, "

                f"threshold=0.800, "

                f"location={level_up_location}, "

                f"size={level_up_size}"

            )

            logger.info(

                "未检测到升级窗口，确认可以点击 next"

            )

        # ==================================
        # 7. 点击 next
        # ==================================

        logger.info(
            f"准备点击 next："
            f"location={location}, "
            f"size={size}"
        )

        x, y = location
        width, height = size

        click_window(
            x,
            y,
            width,
            height,
            0.5
        )

        logger.info("next 点击完成")

        # ==================================
        # 8. 战斗流程结束
        # ==================================

        logger.info("战斗流程结束")

        return