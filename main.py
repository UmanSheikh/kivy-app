from cProfile import label
import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random

class Function(BoxLayout):
    def __init__(self):
        super(Function, self).__init__()

    def rock(self):
        self.Check('r')
    def paper(self):
        self.Check('p')
    def scissors(self):
        self.Check('s')

    def Check(self, user_input):
        cpu = ['r', 'p', 's']
        choice = random.choice(cpu)
        if choice == 'r':
            self.cpu_id.text = 'CPU selected Rock'
        elif choice == 'p':
            self.cpu_id.text = 'CPU selected Paper'
        elif choice == 's':
            self.cpu_id.text = 'CPU selected Scissors'


        if user_input == choice:
            label = 'Draw'
        elif user_input == 'r' and choice == 'p':
            label = 'You Lose'
        elif user_input == 'r' and choice == 's':
            label = 'You Win'
        elif user_input == 'p' and choice == 'r':
            label = 'You Win'
        elif user_input == 'p' and choice == 's':
            label = 'You Lose'
        elif user_input == 's' and choice == 'r':
            label = 'You Lose'
        elif user_input == 's' and choice == 'p':
            label = 'You Win'
        self.check.text = label

class SWcodes(App):
    def build(self):
        return Function()


if __name__ == '__main__':
    SWcodes().run()