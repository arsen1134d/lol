# class Shifrator:
#
#     def __init__(self,a, b):
#         self.__a = a
#         self.__b = b
#
#     def __result(self):
#         return self.__a * self.__b/5
#
#     def get_result(self):
#         return self.__result()
#
#
# sh = Shifrator(5,6 )
# print(sh.get_result())


#
# class Number1:
#     test_number = 3
#
#     def __init__(self, number, number_2):
#         self._number1 = number
#         self._number2 = number_2
#         self._test_number2 = 1
#         self._test_number3 = 2
#
#     def __privat_numbers(self, number_3):
#         self._number3 = number_3
#         self._number4 = 4
#         self._number34 = self.__number3 + self._number4
#
#     def __not_privat(self, number5 ):
#         self._number5 = number5
#         self._number6 = 6
#
# class Number(Number1):
#
#     def __privat_numbers(self, number7):
#         self.__number7 = number7
#         self.__number8 = 8
#         print(self.__number7 - self.__number8 - self._number11)
#
#     def __not_privat(self, number9):
#         self._number9 = number9
#         self._number10 = 10
#         print(self._number9 + self._number10 + self._number11)
#
#
# number = Number(3,4)
# number._not_privat_numbers2(10)
# number2 = Number1(4, 2)
# number2._not_privat_number(90)
