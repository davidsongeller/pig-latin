def test_main():
    assert main("hello world") == "ellohay orldway"
    assert main("a sentence") == "aay entencesay"
    assert main("apple") == "appleay"
    assert main("123") == "123"
    assert main("") == ""
