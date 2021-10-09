import os


def find_files(suffix, path):
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
