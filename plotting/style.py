from __future__ import annotations

import matplotlib.pyplot as plt


def apply_origin_style() -> None:
    plt.rcParams["font.family"] = "Arial"
    plt.rcParams["axes.linewidth"] = 1.5
    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["ytick.direction"] = "in"
    plt.rcParams["xtick.major.size"] = 5
    plt.rcParams["ytick.major.size"] = 5
