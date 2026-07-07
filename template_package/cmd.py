import sys
from template_package.module1 import add
from template_package.module2 import prod


def parse_args() -> tuple[float, float]:
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    return x, y


def cmd_add():
    try:
        x, y = parse_args()
        result = add(x, y)
        print(f"add({x}, {y}) = {result}")
    except (IndexError, ValueError):
        print("Error! Usage: template-add <number_1> <number_2>")
        sys.exit(1)


def cmd_prod():
    try:
        x, y = parse_args()
        result = prod(x, y)
        print(f"prod({x}, {y}) = {result}")
    except (IndexError, ValueError):
        print("Error! Usage: template-prod <number_1> <number_2>")
        sys.exit(1)
