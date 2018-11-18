# -*- coding:utf-8 -*-
__author__ = "liaokong"
__time__ = "2018/10/17 15:08"

from PySide import QtGui
from PySide import QtCore

from Utils import *


class ExampleWidget(QtGui.QDialog):
    def __init__(self, parent=None):
        super(ExampleWidget, self).__init__(parent)
        self.v_layout = QtGui.QVBoxLayout(self)

        load_style(self)

        # QLineEdit
        self.line = QtGui.QLineEdit()
        self.line.setMinimumHeight(35)
        self.line.setMinimumWidth(208)
        self.v_layout.addWidget(self.line)

        # QComboBox: combobox_style()
        self.cb = QtGui.QComboBox()
        self.cb.setMinimumHeight(35)
        self.cb.setMinimumWidth(208)
        self.cb.addItems(["aa", "bb", "cc", "dd", "ee"])
        combobox_style(self.cb)
        self.v_layout.addWidget(self.cb)

        list_h_layout = QtGui.QHBoxLayout()

        # QListWidget
        self.list_widget = QtGui.QListWidget()
        self.list_widget.addItems(["aa", "bb", "cc", "dd", "ee"])
        list_h_layout.addWidget(self.list_widget)

        # QTableWidget
        self.table = QtGui.QTableWidget()
        self.table.setRowCount(2)
        self.table.setColumnCount(2)
        aa = QtGui.QTableWidgetItem("aa")
        aa.setTextAlignment(QtCore.Qt.AlignCenter)
        bb = QtGui.QTableWidgetItem("bb")
        bb.setTextAlignment(QtCore.Qt.AlignCenter)
        cc = QtGui.QTableWidgetItem("cc")
        cc.setTextAlignment(QtCore.Qt.AlignCenter)
        dd = QtGui.QTableWidgetItem("dd")
        dd.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table.setItem(0, 0, aa)
        self.table.setItem(1, 0, bb)
        self.table.setItem(0, 1, cc)
        self.table.setItem(1, 1, dd)
        list_h_layout.addWidget(self.table)

        self.v_layout.addLayout(list_h_layout)

        # QProgressBar: progress_style()
        self.pb = QtGui.QProgressBar()
        progress_style(self.pb, "Aqua")
        self.pb.setMinimum(0)
        self.pb.setMaximum(100)
        self.pb.setValue(25)
        self.v_layout.addWidget(self.pb)

        cr_h_layout = QtGui.QHBoxLayout()
        # QCheckBox
        self.cb1 = QtGui.QCheckBox()
        self.cb2 = QtGui.QCheckBox()
        self.cb2.setChecked(True)
        cr_h_layout.addWidget(self.cb1)
        cr_h_layout.addWidget(self.cb2)

        # QRadioButton
        self.rb1 = QtGui.QRadioButton()
        self.rb2 = QtGui.QRadioButton()
        self.rb2.setChecked(True)
        cr_h_layout.addWidget(self.rb1)
        cr_h_layout.addWidget(self.rb2)
        self.v_layout.addLayout(cr_h_layout)

        # QTabWidget: table_style()
        self.tabWidget = QtGui.QTabWidget()
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        table_style(self.table)
        self.horizontalLayout = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tabWidget.setTabText(0, "aa")
        self.tabWidget.setTabText(1, "bb")
        self.tabWidget.setTabText(2, "cc")
        self.v_layout.addWidget(self.tabWidget)

        # QSlider
        self.s = QtGui.QSlider()
        self.s.setOrientation(QtCore.Qt.Horizontal)
        self.v_layout.addWidget(self.s)

        # QCalendarWidget: calendar_style()
        self.cw = QtGui.QCalendarWidget()
        self.cw.setMaximumWidth(280)
        calendar_style(self.cw)
        self.v_layout.addWidget(self.cw)

        # QSpinBox
        self.spinbox = QtGui.QSpinBox()
        self.v_layout.addWidget(self.spinbox)

        # QTreeWidget
        self.treeWidget = QtGui.QTreeWidget()
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setObjectName("treeWidget")
        root = QtGui.QTreeWidgetItem(self.treeWidget)
        root.setText(0, u"用户组")
        root.setExpanded(True)
        self.treeWidget.addTopLevelItem(root)

        item_1 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_1.setText(0, "a")
        item_2 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_2.setText(0, "b")
        item_3 = QtGui.QTreeWidgetItem(item_2)
        item_5 = QtGui.QTreeWidgetItem(item_2)
        item_4 = QtGui.QTreeWidgetItem(item_3)
        item_3.setText(0, "c")
        item_4.setText(0, "d")
        item_5.setText(0, "e")
        self.v_layout.addWidget(self.treeWidget)


if __name__ == '__main__':
    app = QtGui.QApplication([])

    b = ExampleWidget()
    b.show()

    app.exec_()

