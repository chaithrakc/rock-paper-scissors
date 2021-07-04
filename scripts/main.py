import os

from scripts.roshambo import RoShamBo


def load_welcome_banner():
    relative_filepath = os.path.join('', '../resources', 'banner.txt')
    with open(relative_filepath) as file_handler:
        banner_str = file_handler.read()
        print(banner_str)


if __name__ == '__main__':
    load_welcome_banner()
    roshambo = RoShamBo()
    roshambo.play()
