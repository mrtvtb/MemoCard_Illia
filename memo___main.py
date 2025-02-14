from PyQt5.QtWidgets import QApplication
app = QApplication([])

import random

from random import choices, shuffle
from time import sleep

from memo___card_layout import *
from memo___app import *

list_rb = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

class Question(): #клас для створення питання
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question #питання
        self.answer = answer #відповідь
        self.wrong_ans1 = wrong_ans1 #
        self.wrong_ans2 = wrong_ans2 # неправильні відповіді
        self.wrong_ans3 = wrong_ans3 #
        self.actual = True
        self.right_ans = 0 # кількість правильних відповідей
        self.amount_try = 0 #кількість спроб
        self.wrong_attempts = 0

    def got_rigth(self): #метод для відображення, якщо відповідь правильна і рахування статистики
        self.right_ans += 1
        self.amount_try += 1
        self.wrong_attempts = 0

    def got_wrong(self): #метод для відображення, якщо відповідь неправильна і рахування статистики
        self.amount_try += 1
        self.wrong_attempts += 1

    def success_rate(self):
        # Обчислюємо успішність питання (відсоток правильних відповідей)
        if self.amount_try == 0:
            return 0
        return (self.right_ans / self.amount_try) * 100

    def reset_wrong_attempts(self):
        # Метод для скидання лічильника неправильних відповідей, коли питання повертається
        if self.wrong_attempts >= 3:
            self.wrong_attempts = 0

def switch_screen(): #функція яка показує правильний результат, коли натиснута кнопка "Відповісти" і дає наступне питання
    if btn_next.text() == "Відповісти":
        RadioGroupBox.hide()
        AnsGroupBox.show()
        RadioGroup.setExclusive(False)
        check_result()
        btn_next.setText("Наступне питання")
    else:
        RadioGroupBox.show()               
        AnsGroupBox.hide()
        RadioGroup.setExclusive(True)
        new_question()
        btn_next.setText("Відповісти")


def new_question():
    global cur_q

    weights = []
    for q in list_questions:
        q.reset_wrong_attempts()  

        success = q.success_rate() 

        if success > 80:  
            weights.append(0.2)  
        else:
            if q.wrong_attempts >= 3:
                weights.append(1)  
            else:
                weights.append(0.5)  
    
   
    cur_q = random.choices(list_questions, weights=weights, k=1)[0]


    lb_Correct.setText(cur_q.answer)
    lb_Question.setText(cur_q.question)

    answers = [cur_q.answer, cur_q.wrong_ans1, cur_q.wrong_ans2, cur_q.wrong_ans3]
    shuffle(answers)
 
    rbtn_1.setText(answers[0])
    rbtn_2.setText(answers[1])
    rbtn_3.setText(answers[2])
    rbtn_4.setText(answers[3])


def check_result():
    for radio_button in list_rb:
        if radio_button.isChecked():
            if radio_button.text() == lb_Correct.text():
                lb_Result.setText("Правильно")
                cur_q.got_rigth()
                radio_button.setChecked(False)
            else:
                lb_Result.setText("Неправильно")
                cur_q.got_wrong()
                radio_button.setChecked(False)


def rest():
    timer = sp_rest.value()
    window_card.hide()
    sleep(timer)
    window_card.show()

def show_menu():
    right = cur_q.right_ans
    amount = cur_q.amount_try

    if amount != 0:
        percent = (right / amount) * 100
    else:
        percent = 0
            
    answers_count_label.setText(f"Разів відповіли: {amount}")
    correct_count_label.setText(f"Вірних відповідей: {right}")
    success_label.setText(f"Успішність: {round(percent)}%")
    window_card.hide()
    menu_card.show()

def hide_menu():
    menu_card.hide()
    window_card.show()

def clearLine():
    new_q_line.clear()
    new_answer_line.clear()
    new_wrong1_line.clear()
    new_wrong2_line.clear()
    new_wrong3_line.clear()


def addQuestion():
    new_q = new_q_line.text()
    new_ans = new_answer_line.text()
    new_1_wr = new_wrong1_line.text()
    new_2_wr = new_wrong2_line.text()
    new_3_wr = new_wrong3_line.text()
    New_Quest = Question(new_q, new_ans, new_1_wr, new_2_wr, new_3_wr)
    list_questions.append(New_Quest)
    clearLine()


q1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

list_questions = [q1, q2, q3, q4]

new_question()


btn_next.clicked.connect(switch_screen) 
btn_rest.clicked.connect(rest)
btn_menu.clicked.connect(show_menu)
previous.clicked.connect(hide_menu)
clear_button.clicked.connect(clearLine)
add_button.clicked.connect(addQuestion)
app.exec_()