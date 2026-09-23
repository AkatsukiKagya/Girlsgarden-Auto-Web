# automation/action.py

import time

from automation.screenshot import screenshot_canvas
from automation.vision import find_template
from automation.mouse import click_window


def wait_for_template(
    template_path: str,
    threshold: float = 0.8,
    interval: float = 0.5,
    timeout: float = 20.0,
):
    """
    等待指定模板出现。

    :param template_path: 模板图片路径
    :param threshold: 匹配度阈值
    :param interval: 检测间隔
    :param timeout: 超时时间
    :return: score, location, size
    """

    start_time = time.time()

    while True:

        screenshot = screenshot_canvas()

        found, score, location, size = find_template(
            screenshot,
            template_path,
            threshold,
        )

        if found:
            return score, location, size

        if time.time() - start_time >= timeout:
            raise TimeoutError(
                f"等待模板超时：{template_path}"
            )

        time.sleep(interval)


def wait_for_template_gone(
    template_path: str,
    threshold: float = 0.8,
    interval: float = 0.5,
    timeout: float = 20.0,
):
    """
    等待指定模板消失。
    """

    start_time = time.time()

    while True:

        screenshot = screenshot_canvas()

        found, score, location, size = find_template(
            screenshot,
            template_path,
            threshold,
        )

        print(
            f"等待模板消失："
            f"score={score:.3f}, "
            f"found={found}"
        )

        if not found:
            return

        if time.time() - start_time >= timeout:
            raise TimeoutError(
                f"等待模板消失超时：{template_path}"
            )

        time.sleep(interval)


def wait_for_any_template(
    templates: list[tuple[str, str]],
    threshold: float = 0.8,
    interval: float = 0.5,
    timeout: float = 30.0,
):
    """
    等待任意一个模板出现。

    :param templates:
        [
            ("按钮名称", "模板路径"),
            ...
        ]

    :param threshold: 匹配度阈值
    :param interval: 检测间隔
    :param timeout: 超时时间

    :return:
        name,
        score,
        location,
        size
    """

    start_time = time.time()

    template_names = [
        name for name, _ in templates
    ]

    while True:

        # 每次循环重新截图
        screenshot = screenshot_canvas()

        best_match = None

        # 检测所有模板
        for name, template_path in templates:

            found, score, location, size = find_template(
                screenshot,
                template_path,
                threshold,
            )

            if not found:
                continue

            # 如果同时检测到多个按钮，
            # 选择匹配度最高的一个
            if best_match is None or score > best_match[1]:
                best_match = (
                    name,
                    score,
                    location,
                    size,
                )

        # 找到按钮
        if best_match is not None:
            return best_match

        # 超时
        if time.time() - start_time >= timeout:
            raise TimeoutError(
                f"30秒内未检测到任何按钮：{template_names}"
            )

        time.sleep(interval)


def wait_and_click(
    template_path: str,
    threshold: float = 0.8,
    interval: float = 0.5,
    timeout: float = 20.0,
):
    """
    等待指定模板出现，找到后点击。
    """

    score, location, size = wait_for_template(
        template_path,
        threshold,
        interval,
        timeout,
    )

    x, y = location
    width, height = size

    click_window(
        x,
        y,
        width,
        height,
    )