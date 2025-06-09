import os

class FileHandler:
    def __init__(self, filename):
        self._filename = filename

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        self._filename = value

    def read_lines(self):
        with open(self._filename, 'r') as file:
            for line in file:
                yield line.strip()

    # ✅ Static method: check if file exists
    @staticmethod
    def file_exists(path):
        return os.path.exists(path)

    # ✅ Class method: create object from path
    @classmethod
    def from_path(cls, path):
        return cls(path)

    # ✅ String representation
    def __str__(self):
        return f"FileHandler('{self._filename}')"

    # ✅ Add method: combine contents of two files into a new file
    def __add__(self, other):
        new_file = "combined.txt"
        with open(self._filename, 'r') as f1, open(other.filename, 'r') as f2, open(new_file, 'w') as fout:
            fout.write(f1.read())
            fout.write("\n")
            fout.write(f2.read())
        return FileHandler(new_file)
