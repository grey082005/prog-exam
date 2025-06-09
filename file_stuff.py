class SimpleReader:
    def __init__(self, filename):
        self._filename = filename  # "Private" style

    @property
    def filename(self):
        return self._filename

    @property
    def line_count(self):
        return sum(1 for _ in open(self._filename))

    def read_lines(self):
        with open(self._filename, 'r') as f:
            for line in f:
                yield line.strip()

    def greet(self):
        return "Hi from SimpleReader!"


class FileCombiner(SimpleReader):
    def __add__(self, other):
        output = "combined.txt"
        with open(self.filename, 'r') as f1, open(other.filename, 'r') as f2, open(output, 'w') as out:
            out.write(f1.read())
            out.write("\n")
            out.write(f2.read())
        return FileCombiner(output)

    def combine_multiple(self, *others):
        with open(self.filename, 'a') as out:
            for other in others:
                with open(other.filename, 'r') as f:
                    out.write("\n")
                    out.write(f.read())
