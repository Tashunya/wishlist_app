from PyQt5.QtWidgets import QDialog, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QMessageBox


class CreateWishWindow(QDialog):
    def __init__(self, parent=None, dbu=None):
        super(CreateWishWindow, self).__init__(parent)
        self.dbu = dbu
        QDialog.__init__(self)
        self.setupUi(self)

    def setupUi(self, item_window):
        item_window.setObjectName('Я хочу...')
        item_window.resize(500, 500)

        vbox = QVBoxLayout()

        self.name = QLineEdit()
        self.name.setPlaceholderText('Название')
        vbox.addWidget(self.name)
        self.price = QLineEdit()
        self.price.setPlaceholderText('Цена')
        vbox.addWidget(self.price)
        self.link = QTextEdit()
        self.link.setPlaceholderText('Ссылка')
        vbox.addWidget(self.link)
        self.comment = QTextEdit()
        self.comment.setPlaceholderText('Примечание')
        vbox.addWidget(self.comment)

        self.submit_btn = QPushButton('Сохранить', self)
        self.close_btn = QPushButton('Закрыть', self)
        vbox.addWidget(self.submit_btn)
        vbox.addWidget(self.close_btn)
        self.setLayout(vbox)

        self.submit_btn.clicked.connect(self.add_new_wish)
        self.close_btn.clicked.connect(self.close_window)
        self.show()

    def add_new_wish(self):
        if self.name.text() != "":
            cmd = f"INSERT INTO `{self.dbu.table_name}` (`name`, `price`, `link`, `comment`)"
            cmd += f" VALUES ('{self.name.text()}', '{self.price.text()}'," \
                   f" '{self.link.toPlainText()}', '{self.comment.toPlainText()}')"
            self.dbu.run_command(cmd)
            self.dbu.cnx.commit()
            alert = QMessageBox()
            print("Закоммичено")
            alert.setText("Желание сохранено")
            alert.exec_()
            self.close_window()
        else:
            alert = QMessageBox()
            alert.setText('Заполните поле "Я хочу"')
            alert.exec_()

    def close_window(self):
        self.close()