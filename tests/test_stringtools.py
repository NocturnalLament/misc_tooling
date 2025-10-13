from src.misc_tooling.string_builder import StringBuilder

class TestStringTools:
    def test_build_string(self):
        s = StringBuilder("This", "is", "a", "test")
        assert s.render() == "This is a test"

    def test_drop_from_string(self):
        s = StringBuilder("This", "is", "a", "test")
        s.drop_string("is")
        assert s.render() == "This a test"

    def test_replace(self):
        s = StringBuilder("This", "is", "a", "test")
        s.replace("test", "big test")
        assert s.render() == "This is a big test"

    def test_replace_at_index(self):
        s = StringBuilder("This", "Is", "a", "test")
        s.replace_at_index(1, "is")
        assert s.render() == "This is a test"