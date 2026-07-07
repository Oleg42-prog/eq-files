import os
import sys


def parse_args() -> tuple[bool, str, str]:
    is_args_valid = True
    file_path_a = sys.argv[1]
    file_path_b = sys.argv[2]

    if not os.path.exists(file_path_a):
        is_args_valid = False
        print(f'Path file_path_a is not exists: {file_path_a}')

    if not os.path.exists(file_path_b):
        is_args_valid = False
        print(f'Path file_path_b is not exists: {file_path_b}')

    return is_args_valid, file_path_a, file_path_b


def is_eq_files(path_a: str, path_b: str) -> bool:
    with open(path_a, 'rb') as file_a:
        with open(path_b, 'rb') as file_b:
            return file_a.read() == file_b.read()


def dedup_files(path_a: str, path_b: str) -> bool:
    if not is_eq_files(path_a, path_b):
        return False

    os.remove(path_b)

    return not os.path.exists(path_b)


def eq_command(path_a: str, path_b: str):
    is_args_valid, file_path_a, file_path_b = parse_args()
    if not is_args_valid:
        return
    print(is_eq_files(file_path_a, file_path_b))


def dedup_command(path_a: str, path_b: str):
    is_args_valid, file_path_a, file_path_b = parse_args()
    if not is_args_valid:
        return
    print(dedup_files(file_path_a, file_path_b))


def help_command():
    print('octiles <command> <arguments>')
    print('Command list:')
    print('\t- eq <file_path_a> <file_path_b>')
    print('\t- dedup <path_a> <path_b>')
    print('\t- help')


def cmd():
    command = sys.argv[1]
    arguments = sys.argv[2:]
    match command:
        case 'dedup': dedup_command(*arguments)
        case 'eq': eq_command(*arguments)
        case _: help_command()
