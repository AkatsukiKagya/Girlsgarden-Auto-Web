import config
from config import CANVAS_OFFSET_X, CANVAS_OFFSET_Y
from automation.window import *

def screen_to_canvas(screen_x: int, screen_y: int) -> tuple[int, int]:
    """
    屏幕坐标 转化为 Canvas 坐标
    :param screen_x: 屏幕 X 轴坐标
    :param screen_y: 屏幕 Y 轴坐标
    :return: Canvas坐标(x, y)
    """
    return screen_x + CANVAS_OFFSET_X, screen_y + CANVAS_OFFSET_Y

def canvas_to_screen(canvas_x: int, canvas_y: int) -> tuple[int, int]:
    """
    Canvas 坐标转化为 屏幕坐标
    :param canvas_x: Canvas X坐标
    :param canvas_y: Canvas Y坐标
    :return: 屏幕坐标(x, y)
    """
    return config.CURRENT_CANVAS_LEFT + canvas_x, config.CURRENT_CANVAS_TOP + canvas_y