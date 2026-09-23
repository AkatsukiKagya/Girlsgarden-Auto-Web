import pyautogui
import time
import config
from automation.position_calculator import *

def get_mouse_safe_position():
    """
    计算鼠标安全位置
    :return:
    """
    config.current.mouse_safe_x = config.current.canvas_left - 5
    config.current.mouse_safe_y = config.current.canvas_top - 5

def move_to_safe_position():
    """
    move mouse to safe position
    :return: none
    """
    move_to_x = 0
    move_to_y = 0
    move_to_screen(
        move_to_x, move_to_y
    )

    logger.info(f"移动到({move_to_x}, {move_to_y})")


def move_to_canvas(canvas_x, canvas_y):
    """

    :param canvas_x: Canvas x position
    :param canvas_y: Canvas y position
    :return: none
    """
    screen_x, screen_y = canvas_to_screen(canvas_x, canvas_y)
    pyautogui.moveTo(screen_x, screen_y)

def move_to_screen(screen_x, screen_y):
    """

    :param screen_x: screen x position
    :param screen_y: screen y position
    :return: none
    """
    pyautogui.moveTo(screen_x, screen_y)


def click_canvas(canvas_x, canvas_y):
    """
    click event
    :param canvas_x:
    :param canvas_y:
    :return: none
    """
    screen_x, screen_y = canvas_to_screen(canvas_x, canvas_y)
    pyautogui.click(screen_x, screen_y)

def click_screen(screen_x, screen_y):
    """
    click event
    :param screen_x:
    :param screen_y:
    :return: none
    """
    pyautogui.click(screen_x, screen_y)

def click_window(
    x: int,
    y: int,
    width: int,
    height: int,
    pre_click_delay: float = 0.3
):
    """
    点击窗口截图中的目标中心，
    点击完成后将鼠标移动到窗口右下角安全区域。
    """

    # 模板左上角 → 模板中心
    click_x = x + width // 2
    click_y = y + height // 2

    # 窗口坐标 → 屏幕坐标
    screen_x = config.current.canvas_left + click_x
    screen_y = config.current.canvas_top + click_y

    # 移动到按钮
    pyautogui.moveTo(
        screen_x,
        screen_y,
        duration=0.1,
    )

    # 点击前摇
    time.sleep(pre_click_delay)
    # 点击
    pyautogui.click()

    # 移动到安全区域
    margin = 30

    safe_x = config.current.canvas_left + config.current.window_width - margin
    safe_y = config.current.canvas_top + config.current.window_height - margin

    pyautogui.moveTo(
        safe_x,
        safe_y,
        duration=0.1,
    )

    logger.info(
        f"鼠标移动到安全位置：({safe_x}, {safe_y})"
    )

