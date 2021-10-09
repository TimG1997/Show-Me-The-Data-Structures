import os


def find_files(suffix, path):
    if path is None or len(path) <= 0:
        raise ValueError("You have to provide a non-empty path")

    if not os.path.isfile(path) and not os.path.isdir(path):
        raise ValueError("You have to provide a file or directory path")

    return find_files_helper(suffix, path)


def find_files_helper(suffix, path, paths=[]):
    if os.path.isfile(path):
        if path.endswith(suffix):
            paths.append(path)

    else:
        directories = os.listdir(path)
        for directory in directories:  # O(n)
            find_files(suffix, path + '/' + directory)

    return paths
