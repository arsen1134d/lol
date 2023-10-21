#дз 1
# def get_even(nubmer):
#    if not number % 2:
#    return False


# дз 2
# def country_symbol(S):
#    temp = "aeiou"
#    s = s.lower()
#    count_list = 0
#    for list in temp:
#       count_list += s.count(list)
#    return count_list

import random


class Student:

    def __init__(self, name=None):
        self.name = name
        self.alive = True
        self.glandess = 50
        self.progres = 0

        def to_study(self):
            print("Time to study!")
            self.progress += 0.12
            self.glandess -= 0.5

    def to_chill(self):
        print("Time reset")
        self.gladness += 5
        self.progres -= 0.1

    def to_sleep(self):
        print("i will sleep!")
        self.gladness += 3

        def is_alive(self):

            if self.progres < -0.5:
                print("Cast out ....")
                self.alive = False
            elif self.gladnes <= 0:
                print("Depression")
                self.alive = False
            elif self.progres > 5:
                print('Prassed externally.....')


def end_of_day(self):
    print(f"Gladness = {self.gladness}")
    print(f"Gladness = {self.gladness}")

    def live(Self, day):
    day = "Day " + str(day) + " of " + self.name + " life "
    print(f"{day:=^50}")
    live_cube == random.randint(a:1, b:3,)
    if life_cube == 1:
        self.to_study()
    elif live_cube == 2:
        self.to_sleep()
    elif live cube == 3:
        self.to_chill():
    self.end_of_day()
    self.is_elif()
nick = Student(name="Nick")
for i in  range(365):
    if nick.alive == False:
        break
        nick.alive(i)
