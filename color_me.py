__author__ = 'De8ug'


class ColorMe:
    """
    give me color see see...
        ColorMe('somestr').blue()
    """

    def __init__(self, some_str):
        self.color_str = some_str

    def blue(self):
        str_list = ["\033[34;1m", self.color_str, "\033[0m"]
        return ''.join(str_list)  # "\033[34;1m" + self.color_str + "\033[0m"

    def green(self):
        str_list = ["\033[32;1m", self.color_str, "\033[0m"]
        return ''.join(str_list)  # "\033[34;1m" + self.color_str + "\033[0m"

    def yellow(self):
        str_list = ["\033[33;1m", self.color_str, "\033[0m"]
        return ''.join(str_list)  # "\033[34;1m" + self.color_str + "\033[0m"

    def red(self):
        str_list = ["\033[31;1m", self.color_str, "\033[0m"]
        return ''.join(str_list)  # "\033[34;1m" + self.color_str + "\033[0m"


def main():
    ColorMe('somestr').blue()


if __name__ == '__main__':
    main()
