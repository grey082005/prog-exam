from file_stuff import FileCombiner
from decorators import color_text

@color_text
def print_msg(msg):
    return msg

if __name__ == "__main__":
    file1 = FileCombiner("file1.txt")
    file2 = FileCombiner("file2.txt")

    combined = file1 + file2

    print(print_msg("Files combined! Contents below:\n"))

    for line in combined.read_lines():
        print(line)
