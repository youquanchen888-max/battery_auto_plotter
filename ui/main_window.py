from __future__ import annotations

from pathlib import Path

from PySide6.QtWidgets import (
    QFileDialog,
    QLabel,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from automation.landt_controller import export_cex_to_csv
from plotting.cycle_plot import generate_cycle_plot


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("电池测试自动出图软件")
        self.resize(640, 420)

        self.label = QLabel("请选择 .cex / .csv / .xlsx 文件")
        self.upload_btn = QPushButton("上传并开始处理")
        self.upload_btn.clicked.connect(self.select_file)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.upload_btn)
        self.setLayout(layout)

    def select_file(self) -> None:
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "选择文件",
            "",
            "Battery Files (*.cex *.csv *.xlsx)",
        )
        if not file_path:
            return

        try:
            source = Path(file_path)
            if source.suffix.lower() == ".cex":
                data_file = Path(export_cex_to_csv(str(source)))
            else:
                data_file = source

            output_image = generate_cycle_plot(str(data_file))
            QMessageBox.information(self, "成功", f"图像已生成：\n{output_image}")
        except Exception as exc:  # noqa: BLE001
            QMessageBox.critical(self, "错误", str(exc))
