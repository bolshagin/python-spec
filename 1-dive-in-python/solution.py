import sys


def mult(xs: list) -> int:
    res = 0
    for x in xs:
        res += int(x)
    return res


xs = sys.argv[1]
print(mult(xs))
