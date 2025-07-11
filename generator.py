import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtGui import QIcon, QPixmap, QFont
import random
import string

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        QToolTip.setFont(QFont('Segoe UI', 12))

        self.setWindowTitle('GEN')
        self.setWindowIcon(QIcon('password.png'))
        self.setGeometry(1000, 120, 1000, 1500)
        self.card = QFrame(self)
        self.card.setGeometry(50, 50, 900, 1400)
        self.card.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 30px;
            }
            QToolTip { background-color: #F9F9F9; color: #A31621; border: 1px solid #A31621; font-size: 20px; }
        """)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(30)
        shadow.setOffset(0, 10)
        shadow.setColor(Qt.black)
        self.card.setGraphicsEffect(shadow)

        self.setStyleSheet('''
                        background-color: #A31621;
                        font-family: Segoe UI;''')
        
        self.Title = QLabel('PASSWORD GENERATOR', self.card)
        self.Title.setGeometry(120, 60, 675, 100)
        self.Title.setStyleSheet('''
                        font-size: 30px;
                        background-color: #F9F9F9;
                        color: #A31621;
                        font-family: Helvetica;
                        border-radius: 40px;''')
        self.animate_text(self.Title.text(), self.Title)
        self.Title.setAlignment(Qt.AlignCenter)
        
        self.length_slider = QSlider(Qt.Horizontal, self.card)
        self.length_slider.setGeometry(300, 180, 300, 80)
        self.length_slider.setCursor(Qt.PointingHandCursor)
        self.length_slider.setRange(4, 35)
        self.length_slider.setTickInterval(1)
        self.length_slider.setTickPosition(QSlider.TicksBelow)
        self.length_slider.setStyleSheet('''
                        QSlider {
                            background: transparent; 
                        }

                        QSlider::groove:horizontal {
                            border: none;
                            background: #F9F9F9;
                            height: 10px;
                            border-radius: 5px;
                        }

                        QSlider::handle:horizontal {
                            background: #D6242F;
                            border: 2px solid #A31621;
                            width: 22px;
                            height: 22px;
                            margin: -7px 0;
                            border-radius: 11px;
                        }

                        QSlider::handle:horizontal:hover {
                            background: #eb2834;
                        }

                        QSlider::sub-page:horizontal {
                            background: #D6242F;
                            border-radius: 5px;
                        }

                        QSlider::add-page:horizontal {
                            background: #F9F9F9;
                            border-radius: 5px;
                        }
                    ''')


        self.current_length = QLabel(f'{self.length_slider.value()} characters',self.card)
        self.current_length.setStyleSheet('font-family: Segoe UI; font-size: 30px; color: #A31621; background-color: transparent;')
        self.current_length.setGeometry(375, 220, 400, 80)
        self.length_slider.valueChanged.connect(self.password_length)

        self.checkbox = QCheckBox('Uppercase (A-Z)', self.card)
        self.checkbox.setStyleSheet("""
                    QCheckBox {
                        font-size: 35px;
                        color: #A31621;
                        background-color: #F9F9F9;
                        padding: 10px;
                        border-radius: 14px;
                    }
                    QCheckBox::indicator {
                        width: 30px;
                        height: 30px;
                        border: 2px solid #A31621;
                        border-radius: 6px;
                        background: white;
                    }
                     QCheckBox::checked {
                        background-color: #A31621;
                        color: white;
                        border: 2px solid #A31621;
                    }
                    QCheckBox::indicator:checked {
                            background-color: white;
                            border: 2px solid #A31621;
                            image: url(checkmark.png);
                        }
                """)
        self.checkbox.setGeometry(145, 320, 600, 100)
        

        self.checkbox2 = QCheckBox('Lowercase (a-z)', self.card)
        self.checkbox2.setStyleSheet("""
                    QCheckBox {
                        font-size: 35px;
                        color: #A31621;
                        background-color: #F9F9F9;
                        padding: 10px;
                        border-radius: 14px;
                    }
                    QCheckBox::indicator {
                        width: 30px;
                        height: 30px;
                        border: 2px solid #A31621;
                        border-radius: 6px;
                        background: white;
                    }
                     QCheckBox::checked {
                        background-color: #A31621;
                        color: white;
                        border: 2px solid #A31621;
                    }
                    QCheckBox::indicator:checked {
                            background-color: white;
                            border: 2px solid #A31621;
                            image: url(checkmark.png);
                        }
                """)
        self.checkbox2.setGeometry(145, 445, 600, 100)

        self.checkbox3 = QCheckBox('Numbers (0-9)', self.card)
        self.checkbox3.setStyleSheet("""
                    QCheckBox {
                        font-size: 35px;
                        color: #A31621;
                        background-color: #F9F9F9;
                        padding: 10px;
                        border-radius: 14px;
                    }
                    QCheckBox::indicator {
                        width: 30px;
                        height: 30px;
                        border: 2px solid #A31621;
                        border-radius: 6px;
                        background: white;
                    }
                     QCheckBox::checked {
                        background-color: #A31621;
                        color: white;
                        border: 2px solid #A31621;
                    }
                    QCheckBox::indicator:checked {
                            background-color: white;
                            border: 2px solid #A31621;
                            image: url(checkmark.png);
                        }
                """)
        self.checkbox3.setGeometry(145, 570, 600, 100)
        
        self.checkbox4 = QCheckBox('Symbols (!@#&*)', self.card)
        self.checkbox4.setStyleSheet("""
                    QCheckBox {
                        font-size: 35px;
                        color: #A31621;
                        background-color: #F9F9F9;
                        padding: 10px;
                        border-radius: 14px;
                    }
                    QCheckBox::indicator {
                        width: 30px;
                        height: 30px;
                        border: 2px solid #A31621;
                        border-radius: 6px;
                        background: white;
                    }
                     QCheckBox::checked {
                        background-color: #A31621;
                        color: white;
                        border: 2px solid #A31621;
                    }
                    QCheckBox::indicator:checked {
                            background-color: white;
                            border: 2px solid #A31621;
                            image: url(checkmark.png);
                        }
                """)
        self.checkbox4.setGeometry(145, 695, 600, 100)

        self.result = QLineEdit('Your generated password will appear here', self.card)
        self.result.setGeometry(105, 950, 700, 110)
        self.result.setReadOnly(True)
        self.result.setStyleSheet("""
            QLineEdit {
                font-size: 26px;
                color: #A31621;
                background-color: #f7f5f5;
                border: 2px solid #A31621;
                border-radius: 20px;
                padding: 10px;
            }
        """)
        self.result.setAlignment(Qt.AlignCenter)

        self.submit_button = QPushButton('Submit', self.card)
        self.submit_button.setGeometry(260, 830, 400, 80)
        self.submit_button.setStyleSheet('font-size: 30px; background-color: #F9F9F9; color: #A31621; border-radius: 30px; border: 2px solid #A31621;')
        self.submit_button.setCursor(Qt.PointingHandCursor)
        self.submit_button.clicked.connect(self.on_click)

        self.copy = QPushButton(self.card)
        self.copy.setGeometry(725, 970, 70, 70)
        self.copy.setIcon(QIcon('copy.png'))  
        self.copy.setIconSize(QSize(43, 43))
        self.copy.setStyleSheet("""
                        QPushButton {
                            border: none;
                            background-color: transparent;
                        }""")
        self.copy.clicked.connect(self.copy_to_clipboard)
        self.copy.setCursor(Qt.PointingHandCursor)
        self.copy.setVisible(False) 
        self.copy.setToolTip('copy password')

        self.auto = QPushButton(self.card)
        self.auto.setGeometry(120, 970, 70, 70)
        self.auto.setIcon(QIcon('spark.png'))
        self.auto.setIconSize(QSize(43, 43))
        self.auto.setStyleSheet("""
                        QPushButton {
                            border: none;
                            background-color: transparent;
                        }""")
        self.auto.setCursor(Qt.PointingHandCursor)
        self.auto.clicked.connect(self.auto_generate)
        self.auto.setToolTip('Auto-Generate')

        self.line = QLabel(self.card)
        self.line.setPixmap(QPixmap('vert.png').scaled(40, 80))
        self.line.setGeometry(705, 970, 70, 70)
        self.line.setStyleSheet("""
                        QLabel {
                            border: none;
                            background-color: transparent;
                        }""")
        self.line.setVisible(False)

        self.line2 = QLabel(self.card)
        self.line2.setPixmap(QPixmap('vert.png').scaled(40, 80))
        self.line2.setGeometry(165, 970, 70, 70)
        self.line2.setStyleSheet("""
                        QLabel {
                            border: none;
                            background-color: transparent;
                        }""")

        self.strength_title = QLabel('Strength:', self.card)
        self.strength_title.setStyleSheet('font-family: Segoe UI; font-size: 30px; color: #A31621; background-color: transparent; font-weight: bold;')
        self.strength_title.setGeometry(390, 1075, 140, 140)

        self.strength = QSlider(Qt.Horizontal, self.card)
        self.strength.setGeometry(135, 1160, 650, 80)
        self.strength.setRange(0, 4)
        self.strength.setTickInterval(1)
        self.strength.setTickPosition(QSlider.TicksBelow)
        self.strength.setStyleSheet('''
                        QSlider {
                            background: transparent; 
                        }

                        QSlider::groove:horizontal {
                            border: none;
                            background: none;
                            height: 10px;
                            border-radius: 5px;
                        }

                        QSlider::handle:horizontal {
                            background: none;
                            border: 0;
                            width: 22px;
                            height: 22px;
                            margin: -7px 0;
                            border-radius: 11px;
                        }

                        QSlider::handle:horizontal:hover {
                            background: none;
                        }

                        QSlider::sub-page:horizontal {
                            background: none;
                            border-radius: 5px;
                        }

                        QSlider::add-page:horizontal {
                            background: #F9F9F9;
                            border-radius: 5px;
                        }''')
        
        self.display_level = QLabel(self.card)
        self.display_level.setGeometry(328, 1240, 250, 50)
        self.display_level.setStyleSheet('''
                                background-color: transparent;
                                font-size: 35px;
                                font-family: Segoe UI;
                                color: #A31621;''')

        self.display_level.setAlignment(Qt.AlignCenter)
        self.display_level.setText('')

        self.toast = QLabel('', self)
        self.toast.setStyleSheet("""
            QLabel {
                background-color: #A31621;
                color: white;
                font-size: 22px;
                padding: 12px 24px;
                border-radius: 12px;
            }
        """)
        self.toast.adjustSize()
        self.toast.move(735, 955)
        self.toast.hide()

        self.toast_timer = QTimer()
        self.toast_timer.setSingleShot(True)
        self.toast_timer.timeout.connect(self.toast.hide)


    def password_length(self):
        length = self.length_slider.value()
        self.current_length.setText(f'{length} characters')

    def on_click(self):
        length = self.length_slider.value()
        symbo = '!@#$%^&*()-_+|\\[~'

        groups = {
            'up': (self.checkbox.isChecked(), string.ascii_uppercase),
            'low': (self.checkbox2.isChecked(), string.ascii_lowercase),
            'num': (self.checkbox3.isChecked(), string.digits),
            'sym': (self.checkbox4.isChecked(), symbo)
        }

        active_sets = [chars for checked, chars in groups.values() if checked]

        if not active_sets:
            return None

        password = [random.choice(group) for group in active_sets]

      
        all_allowed = ''.join(active_sets)
        while len(password) < length:
            password.append(random.choice(all_allowed))

        random.shuffle(password)
        final_password = ''.join(password)

        
        self.result.setText(final_password)
        self.copy.setVisible(True)
        self.line.setVisible(True)
        self.show_strength(final_password)

    def copy_to_clipboard(self):
        try: 
            clipboard = QApplication.clipboard()
            clipboard.setText(self.result.text())
            self.show_toast("Copied!")
        except Exception as e:
            self.show_toast("Copy failed!")
            print(f"Clipboard error: {e}")

    def show_toast(self, message="Copied!", duration=1500):
        self.toast.setText(message)
        self.toast.adjustSize()
        self.toast.show()
        self.toast_timer.start(duration)


    
    def show_strength(self, password):
        has_lower = any(c in string.ascii_lowercase for c in password)
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_symbol = any(c in '!@#$%^&*()-_+|\\[~' for c in password)

        score = 0
        if len(password) > 15:
            score += 4
        else:
            score += sum([has_lower, has_upper, has_digit, has_symbol])
        
        if len(password) < 8:
            score = 0

        if score >= 4:
            self.strength.setValue(4)
            self.strength.setStyleSheet('''
                        QSlider {
                            background: transparent; 
                        }

                        QSlider::groove:horizontal {
                            border: none;
                            background: none;
                            height: 10px;
                            border-radius: 5px;
                        }

                        QSlider::handle:horizontal {
                            background: none;
                            border: 0;
                            width: 22px;
                            height: 22px;
                            margin: -7px 0;
                            border-radius: 11px;
                        }

                        QSlider::handle:horizontal:hover {
                            background: #34b52f;
                        }

                        QSlider::sub-page:horizontal {
                            background: #34b52f;
                            border-radius: 5px;
                        }

                        QSlider::add-page:horizontal {
                            background: #F9F9F9;
                            border-radius: 5px; }''')
            self.display_level.setText('Very Strong')
        elif score == 3:
            self.strength.setValue(3)
            self.strength.setStyleSheet('''
                        QSlider {
                            background: transparent; 
                        }

                        QSlider::groove:horizontal {
                            border: none;
                            background: none;
                            height: 10px;
                            border-radius: 5px;
                        }

                        QSlider::handle:horizontal {
                            background: none;
                            border: 0;
                            width: 22px;
                            height: 22px;
                            margin: -7px 0;
                            border-radius: 11px;
                        }

                        QSlider::handle:horizontal:hover {
                            background: #d9cd4a;
                        }

                        QSlider::sub-page:horizontal {
                            background: #d9cd4a;
                            border-radius: 5px;
                        }

                        QSlider::add-page:horizontal {
                            background: #F9F9F9;
                            border-radius: 5px; }''')
            self.display_level.setText('Strong')
        elif score == 2:
            self.strength.setValue(2)
            self.strength.setStyleSheet('''
                        QSlider {
                            background: transparent; 
                        }

                        QSlider::groove:horizontal {
                            border: none;
                            background: none;
                            height: 10px;
                            border-radius: 5px;
                        }

                        QSlider::handle:horizontal {
                            background: none;
                            border: 0;
                            width: 22px;
                            height: 22px;
                            margin: -7px 0;
                            border-radius: 11px;
                        }

                        QSlider::handle:horizontal:hover {
                            background: #d19c3f;
                        }

                        QSlider::sub-page:horizontal {
                            background: #d19c3f;
                            border-radius: 5px;
                        }

                        QSlider::add-page:horizontal {
                            background: #F9F9F9;
                            border-radius: 5px; }''')
            self.display_level.setText('Fair')
        else:
            self.strength.setValue(1)
            self.strength.setStyleSheet('''
                        QSlider {
                            background: transparent; 
                        }

                        QSlider::groove:horizontal {
                            border: none;
                            background: none;
                            height: 10px;
                            border-radius: 5px;
                        }

                        QSlider::handle:horizontal {
                            background: none;
                            border: 0;
                            width: 22px;
                            height: 22px;
                            margin: -7px 0;
                            border-radius: 11px;
                        }

                        QSlider::handle:horizontal:hover {
                            background: #9e2929;
                        }

                        QSlider::sub-page:horizontal {
                            background: #9e2929;
                            border-radius: 5px;
                        }

                        QSlider::add-page:horizontal {
                            background: #F9F9F9;
                            border-radius: 5px; }''')
            
            self.display_level.setText('Weak')

    def animate_text(self, full_text, target_label, interval=50):
        self.full_text = full_text
        self.target_label = target_label
        self.current_index = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_text_animation)
        self.timer.start(interval)

    def update_text_animation(self):
        if self.current_index < len(self.full_text):
            self.target_label.setText(self.full_text[:self.current_index + 1])
            self.current_index += 1
        else:
            self.timer.stop()
        
    def auto_generate(self):
        length = random.randint(4, 35)
        symbo = '!@#$%^&*()-_+|\\[~'
        chars = list(string.ascii_letters + string.digits + symbo)
        generated = ''
        for i in range(length):
            generated += random.choice(chars)

        self.result.setText(generated)
        self.copy.setVisible(True)
        self.line.setVisible(True)
        self.show_strength(generated)
        self.checkbox.setChecked(False)
        self.checkbox2.setChecked(False)
        self.checkbox3.setChecked(False)
        self.checkbox4.setChecked(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec_())