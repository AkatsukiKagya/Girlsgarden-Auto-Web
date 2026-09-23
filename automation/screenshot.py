import mss
import numpy as np
import cv2

import config

def screenshot_canvas(hwnd = config.current.hwnd):
    """
    截图
    :param
    :return: 返回截图
    """
    # 获取 Canvas 的屏幕位置
    canvas_x = config.current.canvas_left
    canvas_y = config.current.canvas_top

    # 计算截屏大小与位置
    canvas_width = config.current.window_width - 2 * config.CANVAS_OFFSET_X
    canvas_height = config.CANVAS_HEIGHT

    monitor = {
        "left": canvas_x,
        "top": canvas_y,
        "width": canvas_width,
        "height": canvas_height,
    }

    with mss.MSS() as sct:
        screenshot = sct.grab(monitor)

    image = np.array(screenshot)
    image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

    return image
