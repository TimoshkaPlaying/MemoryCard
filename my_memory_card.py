from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import random


# Window ----------------------------
app = QApplication([])
main_win = QWidget()
main_win.show()
main_win.setWindowTitle('Memory Card')
main_win.setFixedSize(600, 600)
main_win.cur_question = -1
main_win.total = -1
main_win.score = 0
class Question():
    def __init__(self, question, true, false1, false2, false3):
        self.q = question
        self.true = true
        self.false1 = false1
        self.false2 = false2
        self.false3 = false3

def next_question():
    main_win.total += 1
    main_win.cur_question += 1
    if main_win.cur_question >= len(questions):
        # main_win.total = len(questions)
        print('Статистика:')
        print('-Всего вопросов:', main_win.total)
        print('-Правильных ответов:', main_win.score)
        print('-Рейтинг:', main_win.score/main_win.total*100, '%')
        main_win.cur_question = 0
        main_win.score = 0
        main_win.total = 0
    ask(questions[main_win.cur_question])
def button_f():
    """Функция для button"""
    radio_group.hide()
    answers_group.show()
    button.hide()
    next_question_btn.show()
def button_n():
    """Функция для next_question_btn"""
    radio_group.show()
    answers_group.hide()
    button.show()
    next_question_btn.hide()
    next_question()

# Отбражаем штучки на экране --------------------
question = QLabel('Вопрос')
question.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))

button = QPushButton('Ответить')
button.clicked.connect(button_f)
button.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))

next_question_btn = QPushButton('Следующий вопрос')
next_question_btn.clicked.connect(button_n)
next_question_btn.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
next_question_btn.hide()

#Варианты ответов ---------------------------------------------------
radio_group = QGroupBox('Варианты ответов')

radio_group.setMinimumWidth(400)
radio_group.setMinimumHeight(150)

radio_btn1 = QRadioButton('1 декабря')
radio_btn2 = QRadioButton('1 января')
radio_btn3 = QRadioButton('31 декабря')
radio_btn4 = QRadioButton('31 января')

hbox_radio = QHBoxLayout()
vbox1_radio = QVBoxLayout()
vbox2_radio = QVBoxLayout()

vbox1_radio.addWidget(radio_btn1, alignment=Qt.AlignHCenter)
vbox1_radio.addWidget(radio_btn2, alignment=Qt.AlignHCenter)
vbox2_radio.addWidget(radio_btn3, alignment=Qt.AlignHCenter)
vbox2_radio.addWidget(radio_btn4, alignment=Qt.AlignHCenter)

hbox_radio.addLayout(vbox1_radio)
hbox_radio.addLayout(vbox2_radio)

radio_group.setLayout(hbox_radio)
radio_group.setFont(QtGui.QFont("Times", 10))
#Правильно\Неправильно ---------------------------------------------------
answers_group = QGroupBox('Результат теста')

answers_group.setMinimumWidth(400)
answers_group.setMinimumHeight(150)

lbl1 = QLabel('Правильно/Неправильно')
lbl2 = QLabel('Правильно!!!')

hbox_answers = QHBoxLayout()
vbox1_answers = QVBoxLayout()
vbox2_answers = QVBoxLayout()

vbox1_answers.addWidget(lbl1, alignment=Qt.AlignLeft)
vbox1_answers.addWidget(lbl2, alignment=(Qt.AlignHCenter|Qt.AlignHCenter))

hbox_answers.addLayout(vbox1_answers)
hbox_answers.addLayout(vbox2_answers)

answers_group.setLayout(hbox_answers)
answers_group.setFont(QtGui.QFont("Times", 10))
# Layouts -----------------------
hbox1 = QHBoxLayout()
hbox2 = QHBoxLayout()
hbox3 = QHBoxLayout()

vbox_main = QVBoxLayout()

vbox_main.addLayout(hbox1, stretch=2)
vbox_main.addLayout(hbox2, stretch=8)
vbox_main.addStretch(1)
vbox_main.addLayout(hbox3, stretch=1)
vbox_main.addStretch(1)

vbox_main.setSpacing(5)
# Отбражаем штучки на экране --------------------
hbox1.addWidget(question, alignment=Qt.AlignCenter)

hbox2.addWidget(radio_group, alignment=(Qt.AlignHCenter|Qt.AlignVCenter))

hbox2.addWidget(answers_group, alignment=(Qt.AlignHCenter|Qt.AlignVCenter))
answers_group.hide()

hbox3.addWidget(button, alignment=Qt.AlignCenter)

hbox3.addWidget(next_question_btn, alignment=Qt.AlignCenter)
#Переменные----------------------------------------------------
buttons = [radio_btn1, radio_btn2, radio_btn3, radio_btn4]

questions = [Question('Когда новый год?', '1 января', '1 декабря', '31 января', '31 декабря'),
             Question('Как по английски\n будет "Привет"?', 'Hello', 'Buy', 'Cook', 'The privet'),
             Question('Лучшая музыка в мире?', 'Фонк', 'Поп', 'Детская', 'Колыбельная')]
#Функции------------------------------------------------------
def ask(q):
    random.shuffle(buttons)
    question.setText(q.q)
    buttons[0].setText(q.true)
    buttons[1].setText(q.false1)
    buttons[2].setText(q.false2)
    buttons[3].setText(q.false3)
    lbl2.setText(f'Правильный ответ: {q.true}')
def check_answer():
    if buttons[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
    else:
        show_correct('Неправильно!')
def show_correct(text):
    lbl1.setText(text)

button.clicked.connect(check_answer)
# Цикл-----------------------------------------------
next_question()
main_win.setLayout(vbox_main)
app.exec_()