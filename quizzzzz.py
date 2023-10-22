from  PyQt5.QtWidgets import QApplication
from random import choice, shuffle
from time import sleep
app=QApplication([])
from m2 import *
from m3 import *

class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question=question
        self.answer=answer
        self.wrong_answer1=wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
q10=Question('Дата початку Другої Світової війниЖ', "1 вересня 1939", "28 липня 1914", "22 червня 1941", "2 вересня 1945")
q2=Question('Найвідданіший союзник А. Гітлера:', "Угорщина", "Румунія", "СРСР", "Італія")
q3=Question('Між якими державами було підписано пакт Молотова-Ріббентропа?', "Німеччина та СРСР", "СРСР та США", "Німеччина та Італія", "СРСР та Велика Британія")
q4=Question('Яка держава зазнала найбільших втрат у війні?', "СРСР", "Китай", "Німеччина", "Велика Британія")
q5=Question('Операція "Барбароса" - це план захоплення...', "СРСР", "Франції", "Великої Британії", "Польщі")
q6=Question('', "Правильна відповідь", "Перша неправильна", "Друга неправильна", "Третя неправильна")
q7=Question('Питання7', "Правильна відповідь", "Перша неправильна", "Друга неправильна", "Третя неправильна")
q8=Question('Питання8', "Правильна відповідь", "Перша неправильна", "Друга неправильна", "Третя неправильна")
q9=Question('Питання9', "Правильна відповідь", "Перша неправильна", "Друга неправильна", "Третя неправильна")
q10=Question('Питання10', "Правильна відповідь", "Перша неправильна", "Друга неправильна", "Третя неправильна")





def menu_generation():
    menu_win.show()
    window.hide()
btn_menu.clicked.connect(menu_generation)

def back_menu():
    menu_win.hide()
    window.show()
btn_back.clicked.connect(back_menu)

window.show()
app.exec_()