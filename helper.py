# -*- coding: utf-8 -*-
# Time    : 2020/11/10 20:08
# Author  : LiaoKong
try:
    from PySide2.QtWidgets import *
    from PySide2.QtCore import *
    from PySide2.QtGui import *
except:
    from PySide.QtCore import *
    from PySide.QtGui import *

from Utils import *


class WidgetHelper(object):
    def __init__(self, parent, load_qflat=False):
        self.parent = parent
        self.load_qflat = load_qflat
        if self.load_qflat:
            load_style(self.parent)

    def btn(self, text, obj_name=None, max_w=None, max_h=None, min_w=None,
            min_h=None, btn_style='Aqua', enabled=True, **signals):
        btn = QPushButton(text)
        if self.load_qflat:
            button_style(btn, btn_style)
        self._default_setting(btn, enabled, obj_name, max_w, max_h, min_w, min_h,
                              signals)
        return btn

    def line_edit(self, text='', obj_name=None, max_w=None, max_h=None, min_w=None,
                  min_h=None, placeholder='', enabled=True, **signals):
        line_edit = QLineEdit()
        line_edit.setText(text)
        line_edit.setPlaceholderText(placeholder)
        self._default_setting(line_edit, enabled, obj_name, max_w, max_h, min_w,
                              min_h, signals)
        return line_edit

    def int_line(self, value=0, obj_name=None, max_w=None, max_h=None, min_w=None,
                 min_h=None, enabled=True, **signals):
        int_line = QSpinBox()
        int_line.setValue(value)
        self._default_setting(int_line, enabled, obj_name, max_w, max_h, min_w,
                              min_h, signals)
        return int_line

    def float_line(self, value=0.0, obj_name=None, max_w=None, max_h=None, min_w=None,
                   min_h=None, enabled=True, **signals):
        float_line = QDoubleSpinBox()
        float_line.setValue(value)
        self._default_setting(float_line, enabled, obj_name, max_w, max_h, min_w,
                              min_h, signals)
        return float_line

    def progress(self, value=0, obj_name=None, max_w=None, max_h=None, min_w=None,
                 min_v=0, max_v=100, style='Grass', min_h=None, enabled=True,
                 **signals):
        progress = QProgressBar()
        if self.load_qflat:
            progress_style(progress, style)
        progress.setValue(value)
        progress.setMinimum(min_v)
        progress.setMaximum(max_v)

        self._default_setting(progress, enabled, obj_name, max_w, max_h, min_w,
                              min_h, signals)

        return progress

    def label(self, text, obj_name=None, max_w=None, max_h=None, min_w=None,
              min_h=None):
        label = QLabel(text)
        self._default_setting(label, True, obj_name, max_w, max_h, min_w, min_h)
        return label

    def checkbox(self, text, obj_name=None, max_w=None, max_h=None, min_w=None,
                 min_h=None, checked=False, enabled=True, **signals):
        checkbox = QCheckBox(text)
        checkbox.setChecked(checked)
        self._default_setting(checkbox, enabled, obj_name, max_w, max_h, min_w,
                              min_h, signals)
        return checkbox

    def combobox(self, items=None, obj_name=None, max_w=None, max_h=None, min_w=None,
                 min_h=None, enabled=True, **signals):
        combobox = QComboBox()
        if self.load_qflat:
            combobox_style(combobox)
        if items:
            combobox.addItems(items)
        self._default_setting(combobox, enabled, obj_name, max_w, max_h, min_w, min_h,
                              signals)
        return combobox

    def list(self, items=None, obj_name=None, max_w=None, max_h=None, min_w=None,
             min_h=None, enabled=True, **signals):
        list_widget = QListWidget()
        if items:
            list_widget.addItems(items)
        self._default_setting(list_widget, enabled, obj_name, max_w, max_h, min_w,
                              min_h, signals)
        return list_widget

    def table(self, headers=None, grid=False, obj_name=None, max_w=None, max_h=None,
              min_w=None, min_h=None, enabled=True, **signals):
        table = QTableWidget()
        if headers:
            table.setColumnCount(len(headers))
            table.setHorizontalHeaderLabels(headers)

        if self.load_qflat and grid:
            table_style(table)
        self._default_setting(table, enabled, obj_name, max_w, max_h, min_w, min_h,
                              signals)
        return table

    @staticmethod
    def h_spacer(w=300, h=20):
        return QSpacerItem(w, h, QSizePolicy.Expanding, QSizePolicy.Minimum)

    @staticmethod
    def v_spacer(w=20, h=300):
        return QSpacerItem(w, h, QSizePolicy.Minimum, QSizePolicy.Expanding)

    @staticmethod
    def _default_setting(obj, enabled, obj_name=None, max_w=None, max_h=None,
                         min_w=None, min_h=None, signals=None):
        obj.setEnabled(enabled)

        if obj_name:
            obj.setObjectName(obj_name)
        if max_w:
            obj.setMaximumWidth(max_w)
        if max_h:
            obj.setMaximumHeight(max_h)
        if min_w:
            obj.setMinimumWidth(min_w)
        if min_h:
            obj.setMinimumHeight(min_h)

        if signals:
            for signal_name, func in signals.items():
                getattr(obj, signal_name).connect(func)

    def v_layout(self, widgets, parent=None, spacing=None, margins=None):
        return self._layout(QVBoxLayout, widgets, parent, spacing, margins)

    def h_layout(self, widgets, parent=None, spacing=None, margins=None):
        return self._layout(QHBoxLayout, widgets, parent, spacing, margins)

    def _layout(self, layout_obj, widgets, parent=None, spacing=None, margins=None):
        if parent:
            layout = layout_obj(parent)
        else:
            layout = layout_obj()

        if spacing:
            layout.setSpacing(spacing)

        if margins:
            layout.setContentsMargins(*margins)

        for widget in widgets:
            self._layout_add_items(layout, widget)

        return layout

    @staticmethod
    def _layout_add_items(layout, widget):
        if isinstance(widget, QLayout):
            layout.addLayout(widget)
        elif isinstance(widget, QWidget):
            layout.addWidget(widget)
        elif isinstance(widget, QSpacerItem):
            layout.addItem(widget)
        else:
            raise Exception('Type is not supported.')
