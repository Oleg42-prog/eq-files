import os


def is_eq_files(path_a: str, path_b: str) -> bool:
    with open(path_a, 'rb') as file_a:
        with open(path_b, 'rb') as file_b:
            return file_a.read() == file_b.read()


def dedup_files(path_a: str, path_b: str) -> bool:
    if not is_eq_files(path_a, path_b):
        return False

    os.remove(path_b)

    return not os.path.exists(path_b)
