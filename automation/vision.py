import config
import cv2
import numpy as np
from pathlib import Path
from logger import logger
from automation.mouse import click_window


def find_template(
    image: np.ndarray,
    template_path: str,
    threshold: float = 0.8,
) -> tuple[bool, float, tuple[int, int], tuple[int, int]]:

    if not isinstance(template_path, (str, Path)):
        raise TypeError(
            f"template_path 必须是字符串或 Path，"
            f"实际类型：{type(template_path)}，"
            f"值：{template_path!r}"
        )

    template = cv2.imread(template_path)

    if template is None:
        raise FileNotFoundError(f"找不到模板图片: {template_path}")

    result = cv2.matchTemplate(
        image,
        template,
        cv2.TM_CCOEFF_NORMED,
    )

    _, max_score, _, max_location = cv2.minMaxLoc(result)

    max_location = tuple(map(int, max_location))

    h, w = template.shape[:2]

    found = max_score >= threshold

    return found, max_score, max_location, (w, h)
