import os
from tempfile import gettempdir


class File:

    def __init__(self, path):
        self.path_to_file = path
        if not os.path.exists(path):
            with open(path, 'w'):
                pass

    def read(self):
        with open(self.path_to_file, 'r') as f:
            res = f.read()
        return res

    def write(self, text, mode='w'):
        with open(self.path_to_file, mode) as f:
            f.write(text)

    def __add__(self, other):
        new_path = os.path.join(gettempdir(), 'temp.txt')
        new_file = File(new_path)

        new_file.write(self.read(), 'w')
        new_file.write(other.read(), 'a')
        return new_file

    def __iter__(self):
        self.current_position = 0
        return self

    def __next__(self):
        with open(self.path_to_file, 'r') as f:
            f.seek(self.current_position)
            line = f.readline()
            if not line:
                self.current_position = 0
                raise StopIteration('End of file')

            self.current_position = f.tell()

        return line

    def __repr__(self):
        return os.path.abspath(self.path_to_file)


if __name__ == '__main__':
    path_to_file = 'some_filename'
    file_obj = File(path_to_file)
    for line in file_obj:
        print(line)
