# config

from dataclasses import dataclass

TITLE_KEYWORD = "マブラヴ"
CANVAS_OFFSET_X = 15
CANVAS_OFFSET_Y = 204
CANVAS_HEIGHT = 720

@dataclass
class Current:

    # HWND
    hwnd: int | None = None

    # 窗口左上角坐标和窗口大小
    window_left: int | None = None
    window_top: int | None = None
    window_width: int | None = None
    window_height: int | None = None

    # 截图宽度
    canvas_width: int | None = None

    # 截图左上角坐标
    canvas_left: int | None = None
    canvas_top: int | None = None

    # 鼠标安全坐标
    mouse_safe_x: int | None = None
    mouse_safe_y: int | None = None

current = Current()