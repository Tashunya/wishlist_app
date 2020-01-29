from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QInputDialog, QLineEdit, QMessageBox
import db_manager
from insert_wish import CreateWishWindow


class Ui_Wishlist(QDialog):
    def __init__(self, database, table_name):
        QDialog.__init__(self)
        self.dbu = db_manager.DatabaseUtility(database, table_name)
        self.setupUi(self)
        # self.update_list()

    def setupUi(self, Wishlist):
        Wishlist.setObjectName("Wishlist")
        Wishlist.resize(663, 560)
        self.centralwidget = QtWidgets.QWidget(Wishlist)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 10, 621, 521))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        # add
        self.pushButton_add = QtWidgets.QPushButton(self.widget)
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout.addWidget(self.pushButton_add)

        # show
        self.pushButton_show = QtWidgets.QPushButton(self.widget)
        self.pushButton_show.setObjectName("pushButton_show")
        # self.pushButton_show.setEnabled(False)
        self.verticalLayout.addWidget(self.pushButton_show)

        # edit
        self.pushButton_edit = QtWidgets.QPushButton(self.widget)
        self.pushButton_edit.setObjectName("pushButton_edit")
        # self.pushButton_edit.setEnabled(False)
        self.verticalLayout.addWidget(self.pushButton_edit)

        # remove
        self.pushButton_remove = QtWidgets.QPushButton(self.widget)
        self.pushButton_remove.setObjectName("pushButton_remove")
        # self.pushButton_remove.setEnabled(False)
        self.verticalLayout.addWidget(self.pushButton_remove)

        #down
        self.pushButton_down = QtWidgets.QPushButton(self.widget)
        self.pushButton_down.setObjectName("pushButton_down")
        self.pushButton_down.setEnabled(False)
        self.verticalLayout.addWidget(self.pushButton_down)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        # close
        self.pushButton_close = QtWidgets.QPushButton(self.widget)
        self.pushButton_close.setObjectName("pushButton_close")
        self.verticalLayout.addWidget(self.pushButton_close)


        self.pushButton_add.clicked.connect(self.pushButton_add_clicked)
        self.pushButton_edit.clicked.connect(self.edit_wish)
        self.pushButton_remove.clicked.connect(self.remove_wish)
        self.pushButton_close.clicked.connect(self.close_app)

        self.horizontalLayout.addLayout(self.verticalLayout)
        Wishlist.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Wishlist)
        self.statusbar.setObjectName("statusbar")
        Wishlist.setStatusBar(self.statusbar)

        self.retranslateUi(Wishlist)
        QtCore.QMetaObject.connectSlotsByName(Wishlist)

        self.wishes = ['Wish 1', 'Wish 2', 'Wish 3']
        self.show_wishes(self.wishes)

    def retranslateUi(self, Wishlist):
        _translate = QtCore.QCoreApplication.translate
        Wishlist.setWindowTitle(_translate("Wishlist", "Wishlist"))
        self.pushButton_add.setText(_translate("Wishlist", "Добавить"))
        self.pushButton_show.setText(_translate("Wishlist", "Показать"))
        self.pushButton_edit.setText(_translate("Wishlist", "Изменить"))
        self.pushButton_remove.setText(_translate("Wishlist", "Удалить"))
        self.pushButton_down.setText(_translate("Wishlist", "Вниз"))
        self.pushButton_close.setText(_translate("Wishlist", "Закрыть"))

    def update_list(self):
        pass

    # add item window
    def pushButton_add_clicked(self):
        self.dialog = CreateWishWindow(self, dbu=self.dbu)

    def show_wishes(self, wishes):
        self.listWidget.addItems(wishes)

    def close_app(self):
        quit()

    def edit_wish(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)

        if item is not None:
            text, ok = QInputDialog.getText(self, 'Изменить', 'Отредактируйте желание',
                                            QLineEdit.Normal, item.text())
            if ok and text is not None:
                item.setText(text)

    def remove_wish(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)

        if item is None:
            return
        reply = QMessageBox.question(self, 'Удалить желание', 'Вы хотите удалить '
                                     + str(item.text()) + '?',
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            item = self.listWidget.takeItem(row)
            del item


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Wishlist = QtWidgets.QMainWindow()
    ui = Ui_Wishlist()
    ui.setupUi(Wishlist)
    Wishlist.show()
    sys.exit(app.exec_())

