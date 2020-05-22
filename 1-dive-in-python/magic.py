import os
from tempfile import gettempdir


class File:

    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def read(self):
        pass

    def write(self, text):
        pass

    def __add__(self, other):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def __repr__(self):
        return self.path_to_file


if __name__ == '__main__':
    file_obj = File('path_to_file')
    print(file_obj)
