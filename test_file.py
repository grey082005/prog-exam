# test_file.py

from file_stuff import SimpleReader, FileCombiner

def test_greet():
    r = SimpleReader("file1.txt")
    assert r.greet() == "Hi from SimpleReader!"

def test_combiner_add(tmp_path):
    # Create temporary files for testing
    f1 = tmp_path / "a.txt"
    f2 = tmp_path / "b.txt"
    f1.write_text("Hello")
    f2.write_text("World")

    comb = FileCombiner(str(f1))
    comb2 = FileCombiner(str(f2))
    result = comb + comb2

    assert isinstance(result, FileCombiner)
    assert (tmp_path / "combined.txt").exists() or result.filename == "combined.txt"
