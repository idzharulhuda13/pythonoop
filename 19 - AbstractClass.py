# abstract base class = abc
from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def click(self):
        pass


class pushButton(Button):

    def click(self):
        print("push button click")


button1 = pushButton()

button1.click()
help(button1)
