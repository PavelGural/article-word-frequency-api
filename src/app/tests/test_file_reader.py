import os
from src.app.utils.file_reader import read_article

def test_read_article():
    test_file = "test.txt"
    with open(test_file, "w") as f:
        f.write("This is a test file.")
    
    content = read_article(test_file)
    assert content == "This is a test file."
    
    os.remove(test_file)
