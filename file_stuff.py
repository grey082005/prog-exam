class SimpleReader:
    def __init__(self, filename):
        self.filename = filename

    def read_lines(self):
        with open(self.filename, 'r') as file:
            for line in file:
                yield line.strip()

    def greet(self):
        return "Hi from SimpleReader!"

class FileCombiner(SimpleReader):
    def __add__(self, other):
        new_file = "combined.txt"
        with open(self.filename, 'r') as f1, open(other.filename, 'r') as f2, open(new_file, 'w') as out:
            out.write(f1.read())
            out.write("\n")
            out.write(f2.read())
        return FileCombiner(new_file)
