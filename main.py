# # # class Human:
# # #
# # #
# # #     def __init__(self, name):
# # #         self.name = name
# # #
# # #
# # #
# # # class Auto:
# # #
# # #
# # #     def __init__(self, brand):
# # #         self.brand = brand
# # #         self.passengers = []
# # #
# # #     def add_passengers(self, human ):
# # #             self.passengers.append(human)
# # #
# # #
# # #     def print_name_names(self):
# # #                 if self.passengers != []:
# # #                     print(f'Names of {self.brand} passengers')
# # #                     for name in self.passengers:
# # #                         print(name.name)
# # #                 else:
# # #                     print(f'No passengers in {self.brand} ')
# # #
# # # nick = Human("Nick")
# # # kate = Human("Kate")
# # # car = Auto("Mersdes")
# # #
# # # car.add_passengers(nick)
# # # car.add_passengers(kate)
# # #
# # # car.print_name_names()
# #
# # import random
# # class Human:
# #
# #     def ___init__(self, name="Human", job=None, home=None, car=None):
# #         self.name = name
# #         self.money = 100
# #         self.gladness = 50
# #         self.satiety = 60
# #         self.job = job
# #         self.home = home
# #         self.car = car
# #
# #     def get_home(self):
# #         self.home = House()
# #
# #     def get_car(self):
# #         self.car = Auto(brands_of_car)
# #
# #     def get_job(self):
# #         if self.car.drive():
# #             pass
# #         else:
# #             self.to_repair()
# #             return
# #         self.job = Job(job_list)
# #
# #
# # class House:
# #     def __init__(self):
# #         self.mess = 0
# #         self.food = 0
# #
# #
# # class Job:
# #
# #     def __init__(self, job_list):
# #      self.job = random.choice(list(job_list))
# #      self.salary = job_list[self.job]['salary']
# #      self.gladness_less = job_list[self.job]['gladness_less']
# #
# # job_list = {
# #        "Java developer": {"salary": 50, "gladness_less": 10},
# #          "Python developer": {"salary": 40, "gladness_less": 3},
# #          "C++ developer": {"salary": 60, "gladness_less": 25},
# #          "Rust developer": {"salary": 70, "gladness_less": 15},
# #         }
# #
# #
# #
# # class Auto:
# #
# #
# #     def __init__(self, brand_list):
# #         self.fuel = brand_list[self.brand]["fuel"]
# #         self.strength = brand_list[self.brand]["strength"]
# #         self.consumption = brand_list[self.brand]["consumption"]
# #         self.consumption = brand_list[self.brand]["consumption"]
# #
# #
# #     def drive(self):
# #      if self.strength > 0 and self.fuel >= self.consumption:
# #        self.fuel -= self.consumption
# #        self.strength -= 1
# #        return True
# #      else:
# #         print("The cat cannot move!")
# #         return False
# #
# #
# #
# # brands_of_car = {
# #     "BMW":{"fuel": 100, "strength": 100, "consumption": 6},
# #     "Lada":{"fuel": 50, "strength": 40, "consumption": 10},
# #     "Volvo":{"fuel": 80, "strength": 150, "consumption": 8},
# #     "Ferrari":{"fuel": 80, "strength": 120, "consumption": 14}
# # }
#
#
#
#
# import random
# class Human:
#
#
# def __init___(self, name="Human", job=None, car=None, home=None):
#     self.name = name
#     self.money = 100
#     self.gladness = 50
#     self.satiety = 50
#     self.job = job
#     self.car = car
#     self.home =home
# def eat(self):
#           if self.home <= 0:
#               self.shoping("food")
#           else:
#               if self.satiety >= 100:
#                  self.satiety = 100
#                 return
#               self.satiety += 5
#               self.home.food -= 5
# def work(self):
#     if self.car.drive():
#         pass
#     else:
#         if self.car.fuel < 20
#             self.shopping("fuel")
#             return
#         else:
#             self.to_repair()
#     self.money += self.job.salary
#     self.gladnes  -= self.job.gladnse_less
#     self.satiety -= 4
#
#
# def shopping(self,manage):
#     if self.car.drive():
#         pass
#     else:
#         if self.car.fuel < 20:
#             manage = 'fuel'
#         else:
#             self.to_repair()
#             return
#         if manage == "fuel":
#             print("I bought fuel!")
#             self.money -= 100
#             self.car.fuel += 100
#         elif manage == 'food':
#             print('I bought food')
#             self.money -= 50
#             self.home.food += 50
#         elif manage == "Delicases":
#             print('I happy! delicases')
#             self.gladness += 20
#             self.satiety += 2
#             self.money -= 15
#
#
#                 def days_indexes(self, day):
#                    day = f" Today the {day} of {self.name}'s life "
#                    print(f"{day:=^50}", "\n")
#                    human_indexes = self.name + "'s indexes"
#                    print(f"{human_indexes:^50}", "\n")
#                    print(f"Money – {self.money}")
#                    print(f"Satiety – {self.satiety}")
#                    print(f"Gladness – {self.gladness}")
#                    home_indexes = "Home indexes"
#                    print(f"{home_indexes:^50}", "\n")
#                    print(f"Food – {self.home.food}")
#                    print(f"Mess – {self.home.mess}")
#                    car_indexes = f"{self.car.brand} car indexes"
#                    print(f"{car_indexes:^50}", "\n")
#                    print(f"Fuel – {self.car.fuel}")
#                    print(f"Strength – {self.car.strength}")
#


# class Grandparent:
#     height = 170
#     satiety = 100
#     age = 60
#
# class Parent(Grandparent):
#     age = 40
#
# class  Child(Parent)
#     height = 100
#     def __init__(self):
#         print(self.height)
#         print(self.satiety)
#         print(self.age)
#
# nick =Child()

class Hello_World:
    hello = "Hello"
    _hello = "_Hello"
    __hello = "__Hello"

    def __init__(self):
        self.world = "World"
        self._world = "_World"
        self.__world = "__World"
class Hi(Hello_World):
    def hi_print(self):
        print(self.hello)
        print(self.world)
        print(self._hello)
        print(self._world)
        print(self.__hello)
        print(self.__world)
hello = Hello_World()
hello.printer()
hi = Hi()
hi.hi_print()