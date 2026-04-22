import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вход в систему")
        self.setFixedSize(400, 300)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title_label = QLabel("Авторизация")
        title_label.setFont(QFont("Times New Roman", 16))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        login_label = QLabel("Логин:")
        self.login_input = QLineEdit()
        self.login_input.setFixedWidth(200)
        layout.addWidget(login_label)
        layout.addWidget(self.login_input, alignment=Qt.AlignmentFlag.AlignCenter)

        password_label = QLabel("Пароль:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setFixedWidth(200)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input, alignment=Qt.AlignmentFlag.AlignCenter)

        login_btn = QPushButton("Войти")
        login_btn.clicked.connect(self.login)
        layout.addWidget(login_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        guest_btn = QPushButton("Войти как гость")
        guest_btn.clicked.connect(self.open_guest_window)
        layout.addWidget(guest_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def login(self):
        login = self.login_input.text()
        password = self.password_input.text()

        if not login or not password:
            QMessageBox.warning(self, "Ошибка", "Введите логин и пароль!")
            return

        # В реальной версии проверяется БД
        QMessageBox.critical(self, "Ошибка", "Логин/пароль неверны.")

    def open_guest_window(self):
        self.close()
        self.guest_app = GuestWindow()
        self.guest_app.show()

class GuestWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Обувь - Гость")
        self.setGeometry(100, 100, 1200, 700)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Заголовок (ФИО + роль)
        header = QLabel("Обувь - Гость")
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

        # Таблица товаров
        from widgets.product_list import ProductListWidget
        self.product_widget = ProductListWidget(readonly=True, filters=True)
        layout.addWidget(self.product_widget)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_app = LoginWindow()
    login_app.show()
    sys.exit(app.exec())