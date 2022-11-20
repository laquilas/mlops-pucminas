import sys

def return_path(path_test = "tests"):
    path = sys.path[0]
    for return_folder, folder in enumerate(path.split("\\")):
        if folder == path_test: break
    return_folder = return_folder - len(path.split("\\"))
    # Return folder(s)
    new_path = "\\".join(sys.path[0].split("\\")[:return_folder])
    sys.path.append(new_path)