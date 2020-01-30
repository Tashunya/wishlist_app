from PyQt5.QtWidgets import QDialog, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QMessageBox


class CreateWishWindow(QDialog):
    def __init__(self, parent=None, dbu=None):
        super(CreateWishWindow, self).__init__(parent)
        self.parent = parent
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
        vbox.addWidget(self.submit_btn)
        self.close_btn = QPushButton('Закрыть', self)
        vbox.addWidget(self.close_btn)

        self.setLayout(vbox)

        self.submit_btn.clicked.connect(self.add_new_wish)
        self.close_btn.clicked.connect(self.close_window)

        self.show()

    def add_new_wish(self):
        if self.name.text() != "":
            name, price, link, comment = self.name.text(), self.price.text(), \
                                         self.link.toPlainText(), self.comment.toPlainText()

            self.dbu.add_wish(name, price, link, comment)
            alert = QMessageBox()
            print("Закоммичено")
            alert.setText("Желание сохранено")
            alert.exec_()
            self.close_window()
        else:
            alert = QMessageBox()
            alert.setText('Заполните поле "Название"')
            alert.exec_()

    def close_window(self):
        self.parent.update_table()
        self.close()
