# main.py

from file_stuff import FileCombiner
from decorators import color_text

@color_text("green")
def show_message(msg):
    return msg

def main():
    file1 = FileCombiner("file1.txt")
    file2 = FileCombiner("file2.txt")
    
    combined = file1 + file2  # uses __add__
    print(show_message(f"Files combined into: {combined.filename}"))

    print(">>> Combined file contents:")
    for line in combined.read_lines():
        print(line)

if __name__ == "__main__":
    main()
