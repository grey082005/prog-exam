from file_stuff import SimpleReader

def test_greet():
    reader = SimpleReader("file1.txt")
    assert reader.greet() == "Hi from SimpleReader!"
