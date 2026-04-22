from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class BaseWindow(QMainWindow):
    def __init__(self, title="Обувь", subtitle="Гость"):
        super().__init__()
        self.setFont(QFont("Times New Roman"))
        self.setStyleSheet("background-color: white;")

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        # Заголовок (ФИО + роль)
        header = QLabel(f"{title} - {subtitle}")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setFont(QFont("Times New Roman", 10))
        header.setStyleSheet("background-color: #7FFF00; padding: 8px;")
        layout.addWidget(header)

        # Верхняя панель с кнопкой "Выход"
        top_bar = QWidget()
        top_bar.setFixedHeight(30)
        top_layout = QVBoxLayout(top_bar)
        top_layout.setContentsMargins(0, 0, 10, 0)
        top_layout.setAlignment(Qt.AlignmentFlag.AlignRight)

        exit_btn = QPushButton("Выход")
        exit_btn.setStyleSheet("background-color: #00FA9A; border: none; padding: 4px 12px;")
        exit_btn.setFont(QFont("Times New Roman", 9))
        exit_btn.clicked.connect(self.close)
        top_layout.addWidget(exit_btn)

        layout.addWidget(top_bar)