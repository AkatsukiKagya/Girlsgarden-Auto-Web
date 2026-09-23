# main.py

import time
import config
import logger
from automation.window import get_window_data
from automation.screenshot import *
from automation.mouse import *
from automation.vision import *
from automation.action import *
from flows.battle import *
from logger import logger


def main():
    logger.info("=== Windows AutoScript ===")
    logger.info("自动化程序启动")

    try:
        # ==============================
        # 1. 获取并激活游戏窗口
        # ==============================

        get_window_data()

        activate_window(config.current.hwnd)

        logger.info("窗口已激活")

        time.sleep(0.3)

        # ==============================
        # 2. 主循环
        # ==============================

        while True:
            logger.info("开始检查 MAIN_QUEST")

            # 等待 MAIN_QUEST
            score, location, size = wait_for_template(
                "templates/quest/mainquest/mainquest.png"
            )

            logger.info(
                f"确认当前为 MAIN_QUEST，"
                f"匹配度：{score:.3f}"
            )

            # ==============================
            # 3. 点击 quest_start
            # ==============================

            wait_and_click(
                "templates/quest/mainquest/quest_start.png"
            )

            logger.info("quest_start 点击完成")

            # ==============================
            # 4. 执行战斗流程
            # ==============================

            run_battle()

            logger.info("本次任务完成，准备执行下一轮")

            time.sleep(0.3)






    except KeyboardInterrupt:
        logger.info("\n用户手动停止程序")


    except Exception:
        logger.exception("程序运行发生异常")

    finally:
        logger.info("自动化程序结束")


if __name__ == "__main__":
    main()