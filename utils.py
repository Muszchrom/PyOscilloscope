import os


class PathNotProvidedException(Exception):
    def __init__(self):
        self.message = f"Path is not provided"
        super().__init__(self.message)


class Utils:
    def __init__(self, path):
        if not path:
            raise PathNotProvidedException()
        self.path = path

    def get_files(self):
        files = os.listdir(self.path)
        return files

    def get_pretty_files(self):
        files = os.listdir(self.path)
        strr = "files = [\n"
        for index, file in enumerate(files):
            if index == len(files)-1:
                strr += f"\t{file}\n"
            else:
                strr += f"\t{file},\n"

        strr += "]"
        return strr
