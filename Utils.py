# -*- coding:utf-8 -*-
__author__ = "liaokong"
__time__ = "2018/10/18 16:20"

import os

try:
    from PySide2.QtWidgets import *
    from PySide2.QtCore import *
    from PySide2.QtGui import *
except:
    from PySide.QtCore import *
    from PySide.QtGui import *

from MessageWidget import MessageAsk, Message, InputMessage


def message(msg, msg_type="info", auto_close=True, sec=2.0):
    """
    :param msg: 要展示的信息
    :param msg_type: ['success','info','warning','error']
    :param auto_close: 提示是否自动关闭
    :param sec: 展示秒数
    """
    m = Message(auto_close=auto_close, sec=sec)
    if msg_type == "info":
        m.info(msg)
    elif msg_type == "success":
        m.success(msg)
    elif msg_type == "warning":
        m.warning(msg)
    elif msg_type == "error":
        m.error(msg)
    else:
        raise ValueError

    m.show()
    m.exec_()


def error(msg, auto_close=True, sec=2.0):
    return message(msg, 'error', auto_close, sec)


def success(msg, auto_close=True, sec=2.0):
    return message(msg, 'success', auto_close, sec)


def message_ask(msg, msg_type="info"):
    """
    msg_type:['info','warning']
    """
    ma = MessageAsk()
    if msg_type == "info":
        ma.info(msg)
    elif msg_type == "warning":
        ma.info(msg)
    else:
        raise ValueError

    ma.exec_()

    return ma.status


def input_message(msg, title="提示"):
    im = InputMessage(title, msg)
    im.exec_()

    return im.input_text


def load_style(obj, style="light"):
    """
    style:["light","dark"]
    """
    if style not in ["light", "dark"]:
        style = "light"

    return obj.setStyleSheet(
        open("%s/%s_style.css" % (os.path.dirname(__file__), style)).read().replace(
            "%PATH%", os.path.dirname(__file__).replace("\\", "/")))


def button_style(button, style):
    """
    style:['MediumGray','DarkGray','BlueJeans','Aqua','Mint','Grass','Sunflower','Bittersweet','Grapefruit','Lavender','PinkRose']
    """
    return button.setProperty("class", style)


def combobox_style(combobox):
    return combobox.setItemDelegate(QStyledItemDelegate())


def table_style(table):
    table.setAlternatingRowColors(True)
    table.setShowGrid(False)
    table.setFocusPolicy(Qt.NoFocus)
    try:
        table.horizontalHeader().setResizeMode(QHeaderView.Stretch)
    except:
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


def progress_style(progress, style):
    """
    style:['Aqua','Grass','Sunflower','Grapefruit']
    """
    return progress.setProperty("class", style)


def calendar_style(obj):
    obj.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
    obj.setHorizontalHeaderFormat(QCalendarWidget.NoHorizontalHeader)
