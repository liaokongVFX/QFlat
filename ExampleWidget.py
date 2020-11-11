# -*- coding:utf-8 -*-
__author__ = "liaokong"
__time__ = "2018/10/17 15:08"

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from Utils import *


class ExampleWidget(QDialog):
    def __init__(self, parent=None):
        super(ExampleWidget, self).__init__(parent)
        self.v_layout = QVBoxLayout(self)

        load_style(self)

        # QLineEdit
        self.line = QLineEdit()
        self.line.setMinimumHeight(35)
        self.line.setMinimumWidth(208)
        self.v_layout.addWidget(self.line)

        # QComboBox: combobox_style()
        self.cb = QComboBox()
        self.cb.setMinimumHeight(35)
        self.cb.setMinimumWidth(208)
        self.cb.addItems(["aa", "bb", "cc", "dd", "ee"])
        combobox_style(self.cb)
        self.v_layout.addWidget(self.cb)

        list_h_layout = QHBoxLayout()

        # QListWidget
        self.list_widget = QListWidget()
        self.list_widget.addItems(["aa", "bb", "cc", "dd", "ee"])
        list_h_layout.addWidget(self.list_widget)

        # QTableWidget
        self.table = QTableWidget()
        self.table.setRowCount(2)
        self.table.setColumnCount(2)
        aa = QTableWidgetItem("aa")
        aa.setTextAlignment(Qt.AlignCenter)
        bb = QTableWidgetItem("bb")
        bb.setTextAlignment(Qt.AlignCenter)
        cc = QTableWidgetItem("cc")
        cc.setTextAlignment(Qt.AlignCenter)
        dd = QTableWidgetItem("dd")
        dd.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(0, 0, aa)
        self.table.setItem(1, 0, bb)
        self.table.setItem(0, 1, cc)
        self.table.setItem(1, 1, dd)
        list_h_layout.addWidget(self.table)

        self.v_layout.addLayout(list_h_layout)

        # QProgressBar: progress_style()
        self.pb = QProgressBar()
        progress_style(self.pb, "Aqua")
        self.pb.setMinimum(0)
        self.pb.setMaximum(100)
        self.pb.setValue(25)
        self.v_layout.addWidget(self.pb)

        cr_h_layout = QHBoxLayout()
        # QCheckBox
        self.cb1 = QCheckBox()
        self.cb2 = QCheckBox()
        self.cb2.setChecked(True)
        cr_h_layout.addWidget(self.cb1)
        cr_h_layout.addWidget(self.cb2)

        # QRadioButton
        self.rb1 = QRadioButton()
        self.rb2 = QRadioButton()
        self.rb2.setChecked(True)
        cr_h_layout.addWidget(self.rb1)
        cr_h_layout.addWidget(self.rb2)
        self.v_layout.addLayout(cr_h_layout)

        # QTabWidget: table_style()
        self.tabWidget = QTabWidget()
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        table_style(self.table)
        self.horizontalLayout = QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tabWidget.setTabText(0, "aa")
        self.tabWidget.setTabText(1, "bb")
        self.tabWidget.setTabText(2, "cc")
        self.v_layout.addWidget(self.tabWidget)

        # QSlider
        self.s = QSlider()
        self.s.setOrientation(Qt.Horizontal)
        self.v_layout.addWidget(self.s)

        # QCalendarWidget: calendar_style()
        self.cw = QCalendarWidget()
        self.cw.setMaximumWidth(280)
        calendar_style(self.cw)
        self.v_layout.addWidget(self.cw)

        # QSpinBox
        self.spinbox = QSpinBox()
        self.v_layout.addWidget(self.spinbox)

        # QTreeWidget
        self.treeWidget = QTreeWidget()
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setObjectName("treeWidget")
        root = QTreeWidgetItem(self.treeWidget)
        root.setText(0, u"用户组")
        root.setExpanded(True)
        self.treeWidget.addTopLevelItem(root)

        item_1 = QTreeWidgetItem(self.treeWidget)
        item_1.setText(0, "a")
        item_2 = QTreeWidgetItem(self.treeWidget)
        item_2.setText(0, "b")
        item_3 = QTreeWidgetItem(item_2)
        item_5 = QTreeWidgetItem(item_2)
        item_4 = QTreeWidgetItem(item_3)
        item_3.setText(0, "c")
        item_4.setText(0, "d")
        item_5.setText(0, "e")
        self.v_layout.addWidget(self.treeWidget)


if __name__ == '__main__':
    app = QApplication([])

    b = ExampleWidget()
    b.show()

    app.exec_()

