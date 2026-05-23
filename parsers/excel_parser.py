from __future__ import annotations

import pandas as pd


def load_excel(file_path: str) -> pd.DataFrame:
    return pd.read_excel(file_path)
