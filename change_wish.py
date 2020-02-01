from PyQt5.QtWidgets import QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QMessageBox
from insert_wish import CreateWishWindow


class ChangeWishWindow(CreateWishWindow):
    def __init__(self, item_id=None, parent=None, dbu=None):
        self.item_id = item_id
        super().__init__(parent=parent, dbu=dbu)

    def setupUi(self, item_window):
        self.item = self.dbu.get_wish(self.item_id)

        item_window.setWindowTitle(self.item[1])
        item_window.resize(500, 500)
        vbox = QVBoxLayout()

        self.name = QLineEdit()
        self.name.setText(self.item[1])
        vbox.addWidget(self.name)
        self.price = QLineEdit()
        self.price.setText(self.item[2])
        vbox.addWidget(self.price)
        self.link = QTextEdit()
        self.link.setText(self.item[3])
        vbox.addWidget(self.link)
        self.comment = QTextEdit()
        self.comment.setText(self.item[4])
        vbox.addWidget(self.comment)

        self.submit_btn = QPushButton('Сохранить', self)
        vbox.addWidget(self.submit_btn)
        self.delete_btn = QPushButton('Удалить', self)
        vbox.addWidget(self.delete_btn)
        self.close_btn = QPushButton('Закрыть', self)
        vbox.addWidget(self.close_btn)

        self.setLayout(vbox)

        self.submit_btn.clicked.connect(self.save_edited_wish)
        self.close_btn.clicked.connect(self.close_window)
        self.delete_btn.clicked.connect(self.delete_wish)

        self.show()

    def save_edited_wish(self):
        """
        Save edited wish
        """
        if self.name.text() != "":
            reply = QMessageBox.question(self, 'Сохранение изменений',
                                         f'Сохранить изменения?',
                                         QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                name, price, link, comment = self.name.text(), self.price.text(), \
                                             self.link.toPlainText(), self.comment.toPlainText()
                self.dbu.edit_wish(self.item_id, name, price, link, comment)
                alert = QMessageBox()
                alert.setWindowTitle('Сохранение')
                alert.setText("Желание изменено")
                alert.exec_()
                self.close_window()
        else:
            alert = QMessageBox()
            alert.setWindowTitle('Ошибка')
            alert.setText("Впишите название желания")
            alert.exec_()

    def delete_wish(self):
        """
        Delete wish from db
        """
        reply = QMessageBox.question(self, 'Удалить желание',
                                     f'Вы хотите удалить {self.item[1]}?',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.dbu.del_wish(self.item_id)
            alert = QMessageBox()
            alert.setWindowTitle('Удаление')
            alert.setText("Желание удалено")
            alert.exec_()
            self.close_window()

    def close_window(self):
        super().close_window()
