"""
Rock Paper Scissors Game  https://cs.stanford.edu/people/eroberts/courses/soco/projects/1998-99/game-theory/psr.html

"""
import random
from enum import IntEnum


def load_welcome_banner():
    with open('banner.txt') as file_handler:
        banner_str = file_handler.read()
        print(banner_str)


class RoShamBo:
    class Action(IntEnum):
        Rock = 0
        Paper = 1
        Scissors = 2

    def __init__(self):
        load_welcome_banner()
        self.payoff_matrix = [
            [0, -1, 1],
            [1, 0, -1],
            [-1, 1, 0]
        ]
        self.possible_outcomes = {1: 'You Win!', -1: 'You Lose.', 0: 'It\'s a Tie!'}

    def user_selection(self):
        choices = [f'{action.name}[{action.value}]' for action in self.Action]
        choice_str = ','.join(choices)
        selection = input(f'\nEnter a choice ({choice_str}): ')
        action = self.Action(int(selection))
        return action

    def computer_selection(self):
        selection = random.randint(0, len(self.Action) - 1)
        return self.Action(selection)

    def determine_winner(self, user_action, computer_action):
        print(f'\nYou Chose: {user_action.name}, Computer Chose: {computer_action.name}')
        outcome = self.payoff_matrix[user_action.value][computer_action.value]
        print(self.possible_outcomes[outcome])

    def play(self):
        while True:
            try:
                user_action = self.user_selection()
            except ValueError:
                range_str = f'[0, {len(self.Action) - 1}]'
                print(f'\nInvalid selection. Enter a value in range {range_str}\n')
                continue
            computer_action = self.computer_selection()
            self.determine_winner(user_action, computer_action)
            play_again = input('\nPlay again? (y/n): ')
            if play_again.lower() != 'y':
                break


if __name__ == '__main__':
    roshambo = RoShamBo()
    roshambo.play()
