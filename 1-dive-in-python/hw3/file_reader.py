class FileReader:
    def __init__(self, path: str):
        self.path = path

    def read(self) -> str:
        path, data = self.path, ''
        try:
            with open(path, 'r') as f:
                data = ''.join(f.readlines())
        except FileNotFoundError:
            data = ''
        return data


if __name__ == "__main__":
    fr = FileReader('not_exists_file.txt')
    text = fr.read()
    print(text)

    with open('some_file.txt', 'w') as file:
        file.write('some text')
        file.write('another text')

    fr = FileReader('some_file.txt')
    text = fr.read()
    print(text)
