from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from plotting.style import apply_origin_style

EXPORT_DIR = Path("exports").resolve()


def _infer_columns(df: pd.DataFrame) -> tuple[str, str]:
    candidates_cycle = ["Cycle", "Cycle Index", "循环序号", "循环"]
    candidates_capacity = ["Capacity", "Discharge_Capacity", "放电比容量", "容量"]

    cycle_col = next((c for c in candidates_cycle if c in df.columns), None)
    cap_col = next((c for c in candidates_capacity if c in df.columns), None)
    if cycle_col and cap_col:
        return cycle_col, cap_col

    if df.shape[1] >= 2:
        return df.columns[0], df.columns[1]

    raise ValueError("数据列不足，无法生成循环图。")


def generate_cycle_plot(file_path: str) -> str:
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    path = Path(file_path)
    if path.suffix.lower() == ".csv":
        df = pd.read_csv(path)
    else:
        df = pd.read_excel(path)

    cycle_col, cap_col = _infer_columns(df)

    apply_origin_style()
    plt.figure(figsize=(8, 6))
    plt.plot(df[cycle_col], df[cap_col], linewidth=1.8)
    plt.xlabel("Cycle Number")
    plt.ylabel("Capacity")
    plt.title("Cycle Performance")
    plt.grid(True, alpha=0.3)

    output_path = EXPORT_DIR / "cycle_plot.png"
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
    return str(output_path)
