import sys

def print_ladder(steps: int):
    for step in range(steps):
        print(' ' * (steps - 1 - step) + '#' * (step + 1))

#steps = int(sys.argv[1])
steps = 0
print_ladder(steps)
