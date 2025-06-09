# file_stuff.py

class SimpleReader:
    def __init__(self, filename):
        self.filename = filename

    def read_lines(self):
        # Generator that yields each line without newline
        with open(self.filename, 'r') as f:
            for line in f:
                yield line.strip()

    def greet(self):
        # Simple method to test with pytest
        return "Hi from SimpleReader!"

class FileCombiner(SimpleReader):
    def __add__(self, other):
        # Use + to combine two files into combined.txt
        output = "combined.txt"
        with open(self.filename, 'r') as f1, open(other.filename, 'r') as f2, open(output, 'w') as out:
            out.write(f1.read())
            out.write("\n")
            out.write(f2.read())
        return FileCombiner(output)

    def combine_multiple(self, *others):
        # Append multiple files to this one
        with open(self.filename, 'a') as out:
            for other in others:
                with open(other.filename, 'r') as f:
                    out.write("\n")
                    out.write(f.read())

