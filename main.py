import os
"""


def get_files_and_directories(directory_name):
    files = []
    directories = []
    for entry in os.scandir(directory_name):
        if entry.is_file():
            files.append(entry.name)
        elif entry.is_dir():
            directories.append(entry.name)
    return {'filenames': files, 'dirnames': directories}


directory_name = "patern_directory"
result = get_files_and_directories(directory_name)

print(result)

"""

"""


def sort_files_folders(dictionary, reverse=False):
    sorted_dict = {}
    for key in dictionary:
        sorted_files = sorted(dictionary[key], reverse=reverse)
        sorted_dict[key] = sorted_files
    return sorted_dict


my_dict = {
    "cv_2022": ["file3.txt", "file1.txt", "file2.txt"],
    "cv_2023": ["file2.py", "file1.py", "file3.py"]
}

sorted_dict = sort_files_folders(my_dict)
print(sorted_dict)

sorted_dict = sort_files_folders(my_dict, reverse=True)
print(sorted_dict)

"""


def add_to_dict(d: dict, name: str) -> dict:
    if '.' in name:
        d['files'].append(name)
    else:
        d['folders'].append(name)
    return d


my_dict = {'folders': ['folder1'], 'files': ['file1.txt']}
new_dict = add_to_dict(my_dict, 'folder2')
print(new_dict)

new_dict = add_to_dict(my_dict, 'file2.txt')
print(new_dict)





















