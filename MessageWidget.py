# -*- coding:utf-8 -*-
__author__ = "liaokong"
__time__ = "2018/10/16 14:16"

try:
    from PySide2.QtWidgets import *
    from PySide2.QtCore import *
    from PySide2.QtGui import *
except:
    from PySide.QtCore import *
    from PySide.QtGui import *


class Message(QDialog):
    def __init__(self, auto_close=False, sec=2, parent=None):
        super(Message, self).__init__(parent)

        self.setStyle(QStyleFactory.create("plastique"))

        self.setWindowOpacity(0.98)  # 设置窗口透明度
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)

        self.main_layout = QVBoxLayout(self)

        self.frame = QFrame()
        self.frame_layout = QHBoxLayout()
        self.frame_layout.setSpacing(25)
        self.frame_layout.setContentsMargins(15, 15, 15, 15)
        self.frame.setLayout(self.frame_layout)

        self.btn = QPushButton("x")
        self.btn.clicked.connect(self.close)

        self.label = QLabel()

        self.frame_layout.addWidget(self.label)
        self.frame_layout.addWidget(self.btn)

        self.main_layout.addWidget(self.frame)

        self._sec = sec
        if auto_close:
            self.load_timer()

    def load_timer(self):
        _timer = QTimer(self, timeout=self.close)
        _timer.start(self._sec * 1000)

    def info(self, msg):
        self.setStyleSheet("""
                QFrame{
                    color: black;
                    background-color: #7cd1ef;
                    border-radius: 5px;
                }

                QPushButton {
                    border: 0px solid rgba(255, 255, 255, 0);
                    font-size: 18px;
                    font-family: "Microsoft YaHei";
                    color: rgba(255, 255, 255, 255);
                    padding-bottom: 5px;
                }

                QPushButton:pressed {
                    color: #6cbddc;
                }

                QLabel{
                    color: #31708f;
                    font-weight: 700;
                    font-size: 14px;
                    font-family: "Microsoft YaHei";
                }
                """)

        self.label.setText(msg)

    def success(self, msg):
        self.setStyleSheet("""
                QFrame{
                    color: black;
                    background-color: #b9df90;
                    border-radius: 5px;
                }

                QPushButton {
                    border: 0px solid rgba(255, 255, 255, 0);
                    font-size: 17px;
                    font-family: "Microsoft YaHei";
                    color: rgba(255, 255, 255, 255);
                    padding-bottom: 5px;
                }

                QPushButton:pressed {
                    color: #a0c97f;
                }

                QLabel{
                    color: #325433;
                    font-weight: 700;
                    font-size: 14px;
                    font-family: "Microsoft YaHei";
                }
                """)

        self.label.setText(msg)

    def warning(self, msg):
        self.setStyleSheet("""
                QFrame{
                    color: black;
                    background-color: #ffdd87;
                    border-radius: 5px;
                }

                QPushButton {
                    border: 0px solid rgba(255, 255, 255, 0);
                    font-size: 18px;
                    font-family: "Microsoft YaHei";
                    color: rgba(255, 255, 255, 255);
                    padding-bottom: 5px;
                }

                QPushButton:pressed {
                    color: #e8c677;
                }

                QLabel{
                    color: #8a6d3b;
                    font-weight: 700;
                    font-size: 14px;
                    font-family: "Microsoft YaHei";
                }
                """)

        self.label.setText(msg)

    def error(self, msg):
        self.setStyleSheet("""
                QFrame{
                    color: black;
                    background-color: #f2838f;
                    border-radius: 5px;
                }

                QPushButton {
                    border: 0px solid rgba(255, 255, 255, 0);
                    font-size: 18px;
                    font-family: "Microsoft YaHei";
                    color: rgba(255, 255, 255, 255);
                    padding-bottom: 5px;
                }

                QPushButton:pressed {
                    color: #c16872;
                }

                QLabel{
                    color: #7d2222;
                    font-weight: 700;
                    font-size: 14px;
                    font-family: "Microsoft YaHei";
                }
                """)

        self.label.setText(msg)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.m_flag:
            self.move(event.globalPos() - self.m_Position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


class MessageAsk(QDialog):
    status = False

    def __init__(self, parent=None):
        super(MessageAsk, self).__init__(parent)

        self.setStyle(QStyleFactory.create("plastique"))

        self.setWindowOpacity(0.98)  # 设置窗口透明度
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)

        self.main_layout = QVBoxLayout(self)

        self.frame = QFrame()
        self.frame_layout = QVBoxLayout()
        self.frame.setLayout(self.frame_layout)

        # head_layout
        self.head_layout = QHBoxLayout()

        self.label = QLabel()
        self.head_spacer = QSpacerItem(377, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.close_btn = QPushButton("x")
        self.close_btn.setObjectName("close_btn")
        self.close_btn.clicked.connect(self.close)

        self.head_layout.addWidget(self.label)
        self.head_layout.addItem(self.head_spacer)
        self.head_layout.addWidget(self.close_btn)

        # body
        self.body_browser = QTextBrowser()
        self.body_browser.setMaximumHeight(80)
        self.body_browser.setContextMenuPolicy(Qt.NoContextMenu)

        # footer_layout
        self.footer_layout = QHBoxLayout()
        self.footer_layout.setContentsMargins(15, 0, 0, 15)

        self.yes_btn = QPushButton(u"确定")
        self.yes_btn.setObjectName("yes_btn")
        self.no_btn = QPushButton(u"取消")
        self.no_btn.setObjectName("no_btn")
        self.yes_btn.clicked.connect(self.return_yes)
        self.no_btn.clicked.connect(self.close)

        self.footer_spacer = QSpacerItem(77, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.footer_layout.addWidget(self.yes_btn)
        self.footer_layout.addWidget(self.no_btn)
        self.footer_layout.addItem(self.footer_spacer)

        self.frame_layout.addLayout(self.head_layout)
        self.frame_layout.addWidget(self.body_browser)
        self.frame_layout.addLayout(self.footer_layout)

        self.main_layout.addWidget(self.frame)

    def return_yes(self):
        self.status = True
        self.close()

    def info(self, msg):
        self.setStyleSheet("""
            QFrame{
                color: black;
                background-color: #7cd1ef;
                border-radius: 8px;
            }

            QPushButton#close_btn {
                border: 0px solid rgba(255, 255, 255, 0);
                font-size: 17px;
                font-family: "Microsoft YaHei";
                color: rgba(255, 255, 255, 255);
                padding-right: 15px;
            }

            QPushButton#close_btn:pressed {
                color: #6cbddc;
            }

            QLabel{
                color: #31708f;
                font-weight: 800;
                font-size: 22px;
                font-family: "Microsoft YaHei";
                padding-left: 10px;
                padding-top: 6px;
            }

            QTextBrowser{
                padding-left: 10px;
                padding-top: 2px;
                font-size: 14px;
                font-family: "Microsoft YaHei";
                color: #235a82;
                font-weight: 500;
            }

            QPushButton#yes_btn,#no_btn{
                border: 2px solid #3bafda;
                width: 110px;
                height: 30px;
                border-radius: 4px;
                font-size: 14px;
                font-family: "Microsoft YaHei";
                color: #31709e;
                font-weight: 500;
            }

            QPushButton#yes_btn:hover,#no_btn:hover{
                border: 0px solid rgba(255, 255, 255, 0);
                background-color: #3bafda;
                color: #FFFFFF;
                font-weight: 600;
            }
        """)

        self.label.setText(u"提示")
        self.body_browser.setText(u"    " + msg)

    def warning(self, msg):
        self.setStyleSheet("""
                    QFrame{
                        color: black;
                        background-color: #ffdd87;
                        border-radius: 8px;
                    }

                    QPushButton#close_btn {
                        border: 0px solid rgba(255, 255, 255, 0);
                        font-size: 17px;
                        font-family: "Microsoft YaHei";
                        color: rgba(255, 255, 255, 255);
                        padding-right: 15px;
                    }

                    QPushButton#close_btn:pressed {
                        color: #e9c778;
                    }

                    QLabel{
                        color: #8a6d3b;
                        font-weight: 800;
                        font-size: 22px;
                        font-family: "Microsoft YaHei";
                        padding-left: 10px;
                        padding-top: 6px;
                    }

                    QTextBrowser{
                        padding-left: 10px;
                        padding-top: 2px;
                        font-size: 14px;
                        font-family: "Microsoft YaHei";
                        color: #8a6d3b;
                        font-weight: 500;
                    }

                    QPushButton#yes_btn,#no_btn{
                        border: 2px solid #a77c2d;
                        width: 110px;
                        height: 30px;
                        border-radius: 4px;
                        font-size: 14px;
                        font-family: "Microsoft YaHei";
                        color: #8a6d3b;
                        font-weight: 500;
                    }

                    QPushButton#yes_btn:hover,#no_btn:hover{
                        border: 0px solid rgba(255, 255, 255, 0);
                        background-color: #f6bb42;
                        color: #FFFFFF;
                        font-weight: 600;
                    }
                """)

        self.label.setText(u"警告")
        self.body_browser.setText(u"    " + msg)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.m_flag:
            self.move(event.globalPos() - self.m_Position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


class InputMessage(QDialog):
    input_text = ""

    def __init__(self, title, text, parent=None):
        super(InputMessage, self).__init__(parent)

        self.text = text

        self.setStyle(QStyleFactory.create("plastique"))

        self.setWindowOpacity(0.99)  # 设置窗口透明度
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.setStyleSheet("""
            * {
                font-family: "Microsoft YaHei";
                outline: none;
            }

            QFrame#body_frame {
                background-color: #ffffff;
                border-bottom-right-radius: 8px;
                border-bottom-left-radius: 8px;
                padding-bottom: 6px;
            }

            QFrame#header_frame {
                background-color: #e6e9ed;
                border-top-right-radius: 8px;
                border-top-left-radius: 8px;
            }

            QLabel#header_label{
                font-size: 14px;
                font-weight: 700;
                color: #333333;
                padding-left: 5px;
            }

            QPushButton#close_btn {
                background-color: #e6e9ed;
                border: transparent;
                padding-right: 12px;
                font-size: 14px;
                font-weight: 700;
                color: #333333;
            }

            QPushButton#close_btn:hover {
                color: #4fc1e9;
            }

            QLineEdit {
                border: 1px solid #ccd1d9;
                border-radius: 4px;
                font-size: 14px;
                font-weight: 700;
                padding: 5px 8px;
                selection-background-color: #4fc1e9;
                min-height: 15px;
                margin-top: 5px;
            }

            QLineEdit:focus {
                border: 1px solid #4fc1e9;
            }

            /*QPushButton*/
            QPushButton#finish_btn {
                width: 85px;
                height: 30px;
                color: #fff;
                border: 0px solid rgba(255, 255, 255, 0);
                font-size: 12px;
                font-weight: 700;
                border-radius: 5px;
                background-color: #3bafda;
                margin-right: 8px;
                margin-top: 6px;
            }

            QPushButton#finish_btn:hover {
                background-color: #4fc1e9;
            }

            QPushButton#finish_btn:pressed {
                background: qradialgradient(cx:0.5,
                cy: 0.5,
                fx: 0.5,
                fy: 0.5,
                radius: 1.5,
                stop: 0.2 #4fc1e9,
                stop: 0.8 #3bafda);
            } 
        """)
        self.setMinimumWidth(250)

        main_v_layout = QVBoxLayout(self)
        main_v_layout.setSpacing(0)

        header_frame = QFrame()
        header_frame.setObjectName("header_frame")
        header_h_layout = QHBoxLayout(header_frame)

        header_label = QLabel(title)
        header_label.setObjectName("header_label")
        spacer_item1 = QSpacerItem(50, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        close_btn = QPushButton("x")
        close_btn.setAutoDefault(False)
        close_btn.setObjectName("close_btn")
        close_btn.clicked.connect(self.close)

        header_h_layout.addWidget(header_label)
        header_h_layout.addItem(spacer_item1)
        header_h_layout.addWidget(close_btn)

        body_frame = QFrame()
        body_frame.setObjectName("body_frame")
        body_v_layout = QVBoxLayout(body_frame)

        self.input_line_edit = QLineEdit()
        self.input_line_edit.setPlaceholderText(self.text)
        self.input_line_edit.returnPressed.connect(self.finish_btn_clicked)

        btn_h_layout = QHBoxLayout()

        spacer_item2 = QSpacerItem(50, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        finish_btn = QPushButton("确定")
        finish_btn.setAutoDefault(False)
        finish_btn.setObjectName("finish_btn")
        finish_btn.clicked.connect(self.finish_btn_clicked)

        btn_h_layout.addItem(spacer_item2)
        btn_h_layout.addWidget(finish_btn)

        body_v_layout.addWidget(self.input_line_edit)
        body_v_layout.addLayout(btn_h_layout)

        main_v_layout.addWidget(header_frame)
        main_v_layout.addWidget(body_frame)

    def finish_btn_clicked(self):
        if self.input_line_edit.text():
            self.input_text = self.input_line_edit.text()
            self.close()
        else:
            message(self.text, "error")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.m_flag:
            self.move(event.globalPos() - self.m_Position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


def message(msg, msg_type="info"):
    """
    msg_type:['success','info','warning','error']
    """
    m = Message()
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

    m.exec_()


def message_ask(msg, msg_type="info"):
    """
    msg_type:['info','warning']
    """
    ma = MessageAsk()
    if msg_type == "info":
        ma.info(msg)
    elif msg_type == "warning":
        ma.warning(msg)
    else:
        raise ValueError

    ma.exec_()

    return ma.status


def message_input(msg, title="提示"):
    im = InputMessage(title, msg)
    im.exec_()

    return im.input_text


if __name__ == '__main__':
    app = QApplication([])

    # message(u"Qt is a cross-platform application framework from Qt Software (owned by Nokia).", "success")
    # message(u"Qt is a cross-platform application framework from Qt Software (owned by Nokia).", "info")
    # message(u"Qt is a cross-platform application framework from Qt Software (owned by Nokia).", "warning")
    # message(u"Qt is a cross-platform application framework from Qt Software (owned by Nokia).", "error")
    # print message_ask(u"Qt is a cross-platform application framework from Qt Software (owned by Nokia).")
    # print message_ask(u"Qt is a cross-platform application framework from Qt Software (owned by Nokia).","warning")

    app.exec_()
