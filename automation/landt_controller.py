from __future__ import annotations

import os
import shutil
import time
from pathlib import Path

try:
    from pywinauto.application import Application
except ImportError:  # pragma: no cover
    Application = None  # type: ignore[assignment]

LANDT_EXE = Path(r"C:\Program Files\LAND\蓝电测试系统\land.exe")
EXPORT_DIR = Path("exports").resolve()


def export_cex_to_csv(cex_path: str) -> str:
    """导出 .cex 对应的 CSV。

    当前是“可运行骨架版本”：
    - 如果本机没有蓝电或 pywinauto，退化为复制同目录下同名 CSV（若存在）。
    - 如果有蓝电，先尝试启动蓝电，后续菜单自动化可在此函数中补全。
    """
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    source = Path(cex_path).resolve()
    if not source.exists():
        raise FileNotFoundError(f"未找到输入文件: {source}")

    target = EXPORT_DIR / f"{source.stem}_export.csv"

    sibling_csv = source.with_suffix(".csv")
    if sibling_csv.exists():
        shutil.copyfile(sibling_csv, target)
        return str(target)

    if Application is None:
        raise RuntimeError("未安装 pywinauto，且未找到同名 CSV，无法自动导出。")

    if not LANDT_EXE.exists():
        raise RuntimeError(
            f"未找到蓝电程序: {LANDT_EXE}。\n"
            "请修改 automation/landt_controller.py 中 LANDT_EXE 路径。"
        )

    app = Application(backend="uia").start(str(LANDT_EXE))
    time.sleep(5)
    window = app.top_window()
    print("检测到蓝电窗口:", window.window_text())

    # TODO: 使用 inspect.exe 获取控件信息后，在此补全“打开 cex -> 导出 csv”的菜单流程。

    raise RuntimeError(
        "已启动蓝电，但导出流程尚未录制。"
        "请先用 inspect.exe 确认控件并补全自动化步骤。"
    )
