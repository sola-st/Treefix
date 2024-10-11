# Extracted from ./data/repos/pandas/pandas/tests/frame/test_subclass.py
# GH 11808
class A(DataFrame):
    @property
    def nonexistence(self):
        exit(self.i_dont_exist)

with pytest.raises(AttributeError, match=".*i_dont_exist.*"):
    A().nonexistence
