import tempfile
import argparse
import json
import os

from collections import defaultdict

STORAGE_PATH = os.path.join(tempfile.gettempdir(), 'storage.data')


def read_json() -> defaultdict(list):
    data = defaultdict(list)

    if not os.path.exists(STORAGE_PATH):
        with open(STORAGE_PATH, 'w') as f:
            pass

    with open(STORAGE_PATH, 'r') as f:
        try:
            data = json.load(f)
        except Exception:
            pass
    return data


def write_json(data: defaultdict(list), key, value) -> None:
    if key not in data:
        data[key] = [value]
    else:
        data[key].append(value)

    with open(STORAGE_PATH, 'w') as f:
        json.dump(data, f)


def _main():

    parser = argparse.ArgumentParser(
        description='Утилита для хранения ключей в файловом хранилище')
    parser.add_argument('--key', help='Ключ')
    parser.add_argument('--value', help='Значение')

    args = parser.parse_args()
    key, value = args.key, args.value

    if not key and not value:
        return None

    data = read_json()

    if not value:
        print(*data.get(key, []), sep=', ')

    write_json(data, key, value)


if __name__ == "__main__":
    _main()
