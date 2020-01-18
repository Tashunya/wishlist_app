'''
Написать приложение «Вишлист» с полями:
название,
цена,
ссылка на страницу с покупкой,
примечание
или любое другое маленькое CRUD-приложение на свой вкус.

Требуемые технологии: MySQL, Python + PyQT.

Выложить на GitHub. Ожидаемое время выполнения: 2-4 часа.
'''


from PyQt5.QtWidgets import QApplication, QLabel, \
    QWidget, QPushButton, QVBoxLayout, QMainWindow, QGridLayout
import sys
from wishlist import Ui_Wishlist


class WishlistApp(QMainWindow, Ui_Wishlist):
    def __init__(self, *args, **kwargs):
        super(WishlistApp, self).__init__(*args, **kwargs)
        self.setupUi(self)



def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = WishlistApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
