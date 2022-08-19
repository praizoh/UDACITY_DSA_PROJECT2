import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    files_with_suffix = []
    error = []

    def file_finder(suffix, path):
        if type(suffix) is not str or type(path) is not str or suffix != "" or path != "":
            error.append("Enter right suffix and path")
        # check if path is absolute or relative
        if not os.path.isabs(path):
            path = os.path.join(os.getcwd(), path)
        #  if path is not a directory
        if not os.path.isdir(path):
            error.append("Directory does not exist")
        # list out all directories
        file_listings = os.listdir(path)
        for file in file_listings:
            # if it is a file and ext ends with suffix, print it
            if os.path.isfile((os.path.join(path, file))) and file[-len(suffix):] == suffix:
                files_with_suffix.append(file)
            # if it is a directory, recursion
            elif os.path.isdir((os.path.join(path, file))):
                file_finder(suffix, os.path.join(path, file))
        return files_with_suffix

    try:
        file_finder(suffix, path)
        if len(files_with_suffix) <1:
            return "No file with that extension found"
        return files_with_suffix
    except (FileNotFoundError, IOError, TypeError):
        print("An error occurred")
    return error


print(find_files(".pdf", "testdir"))
print("-----------")
find_files(".c", "./")
print("-----------")
find_files("", "./")
print("-----------")
find_files(".h", "./")
print("-----------")
find_files(".docx", "./")