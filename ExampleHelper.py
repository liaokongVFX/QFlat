# -*- coding: utf-8 -*-
# Time    : 2020/11/10 21:22
# Author  : LiaoKong

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from helper import WidgetHelper


class ExampleWidget(QDialog):
    def __init__(self, parent=None):
        super(ExampleWidget, self).__init__(parent)

        widget_helper = WidgetHelper(self, True)

        self.name_line = widget_helper.line_edit(placeholder=u'请输入姓名')
        header_layout = widget_helper.h_layout(
            [widget_helper.label(u'名字'), self.name_line])

        self.gender = widget_helper.combobox([u'男', u'女', u'保密'], min_w=125)
        body_layout = widget_helper.h_layout(
            [widget_helper.label(u'性别'), self.gender, widget_helper.h_spacer()])

        self.thing_list_widget = widget_helper.list(
            ['a', 'b', 'c'], itemClicked=self.item_clicked)
        self.btn = widget_helper.btn(u'保存', min_h=35, clicked=self.btn_clicked)

        widget_helper.v_layout(
            [
                header_layout,
                body_layout,
                self.thing_list_widget,
                self.btn,
                widget_helper.v_spacer()
            ],
            self, spacing=16)

    def btn_clicked(self):
        print(666)

    def item_clicked(self, item):
        print(item)


if __name__ == '__main__':
    app = QApplication([])

    ew = ExampleWidget()
    ew.setFocus()
    ew.show()

    app.exec_()
