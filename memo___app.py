from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, \
    QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt

card_width, card_height = 600, 500

menu_card = QWidget()
menu_card.resize(card_width, card_height)
menu_card.move(300, 300)

menu_card.setWindowTitle("Список питань")

new_q = QLabel("Питання:")
new_answer = QLabel("Правильна відповідь:")
new_wrong1 = QLabel("Неправильний варіант №1:")
new_wrong2 = QLabel("Неправильний варіант №2:")
new_wrong3 = QLabel("Неправильний варіант №3:")

new_q.setStyleSheet("font-size: 20px")
new_answer.setStyleSheet("font-size: 20px")
new_wrong1.setStyleSheet("font-size: 20px")
new_wrong2.setStyleSheet("font-size: 20px")
new_wrong3.setStyleSheet("font-size: 20px")


new_q_line = QLineEdit("")
new_answer_line = QLineEdit("")
new_wrong1_line = QLineEdit("")
new_wrong2_line = QLineEdit("")
new_wrong3_line = QLineEdit("")

new_q_line.setStyleSheet("font-size: 20px")
new_answer_line.setStyleSheet("font-size: 20px")
new_wrong1_line.setStyleSheet("font-size: 20px")
new_wrong2_line.setStyleSheet("font-size: 20px")
new_wrong3_line.setStyleSheet("font-size: 20px")


add_button = QPushButton("Додати запитання")
add_button.setStyleSheet("font-size: 17px")
clear_button = QPushButton("Очистити")
clear_button.setStyleSheet("font-size: 17px")

stats_label = QLabel("Статистика")
stats_label.setStyleSheet("font-weight: 100; font-size: 35px;")
answers_count_label = QLabel("Разів відповіли: 0")
answers_count_label.setStyleSheet("font-size: 17px")
correct_count_label = QLabel("Вірних відповідей: 0")
correct_count_label.setStyleSheet("font-size: 17px")
success_label = QLabel("Успішність: 0%")
success_label.setStyleSheet("font-size: 17px")

previous = QPushButton("Назад")
previous.setStyleSheet("font-size: 17px")

main_Vlayout = QVBoxLayout()
first_Vlayout = QVBoxLayout()
second_Vlayout = QVBoxLayout()

H1_layout = QHBoxLayout()
H2_layout = QHBoxLayout()


first_Vlayout.addWidget(new_q)
first_Vlayout.addWidget(new_answer)
first_Vlayout.addWidget(new_wrong1)
first_Vlayout.addWidget(new_wrong2)
first_Vlayout.addWidget(new_wrong3)

second_Vlayout.addWidget(new_q_line)
second_Vlayout.addWidget(new_answer_line)
second_Vlayout.addWidget(new_wrong1_line)
second_Vlayout.addWidget(new_wrong2_line)
second_Vlayout.addWidget(new_wrong3_line)

H1_layout.addLayout(first_Vlayout)
H1_layout.addLayout(second_Vlayout)


H2_layout.addWidget(add_button)
H2_layout.addWidget(clear_button)


main_Vlayout.addLayout(H1_layout)
main_Vlayout.addLayout(H2_layout)


main_Vlayout.addWidget(stats_label)
main_Vlayout.addWidget(answers_count_label)
main_Vlayout.addWidget(correct_count_label)
main_Vlayout.addWidget(success_label)


main_Vlayout.addWidget(previous)


menu_card.setLayout(main_Vlayout)

menu_card.hide()
