import win32con
import win32gui

import config
from logger import logger
from config import CANVAS_OFFSET_X, CANVAS_OFFSET_Y


def find_window():
    """
    查找窗口标题中包含 keyword 的窗口
    :return: result = (hwnd, title)
    """

    result = []

    def callback(hwnd, _):
        if not win32gui.IsWindowVisible(hwnd):
            return

        title = win32gui.GetWindowText(hwnd).strip()

        if config.TITLE_KEYWORD in title:
            result.append((hwnd, title))

    win32gui.EnumWindows(callback, None)

    config.current.hwnd = result[0][0]

    return result

def get_window_position():
    """
    获取窗口左上角坐标
    """
    left, top, right, bottom = win32gui.GetWindowRect(config.current.hwnd)
    config.current.window_left = left
    config.current.window_top = top
    config.current.window_width = right - left
    config.current.window_height = bottom - top
    logger.info(f"获取窗口数据成功\n"
                f"窗口左上角({config.current.window_left}, {config.current.window_top})\n"
                f"宽度:{config.current.window_width}\n"
                f"高度:{config.current.window_height}"
                )

def get_canvas_position():
    """
    获取 Canvas 截图窗口 左上角屏幕坐标
    """
    window_x, window_y = config.current.window_left, config.current.window_top

    # 这里暂时根据你的当前 Edge 窗口布局计算
    config.current.canvas_left = window_x + CANVAS_OFFSET_X
    config.current.canvas_top = window_y + CANVAS_OFFSET_Y
    logger.info(f"获取CANVAS左上角坐标成功: ({config.current.canvas_left}, {config.current.canvas_top})")

def get_window_data():
    # 获取 config 中的临时数据
    logger.info("获取HWND, 窗口左上角坐标, canvas左上角坐标数据")

    logger.info("获取HWND")
    windows = find_window()
    logger.info(f"窗口信息{windows}")
    if not windows:
        logger.error("没有找到マブラヴ窗口")
        raise RuntimeError("没有找到マブラヴ窗口")

    logger.info("获取窗口左上角坐标和大小")
    get_window_position()
    get_canvas_position()

    hwnd, title = windows[0]

    logger.info(f"找到窗口：{title}")
    logger.info(f"HWND：{hwnd}")


# 激活窗口测试用函数
def activate_window(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(hwnd)

# 返回窗口大小和位置测试函数
def print_size_and_position(hwnd):
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)

    return f"窗口大小与位置\n左上角: ({left}, {top}), 右下角: ({right}, {bottom})\n宽度: {right - left}, 高度: {bottom - top}"