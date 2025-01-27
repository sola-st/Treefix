# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# Number() is not recognied by PyNumber_Check, so by extension
#  is not recognized by is_scalar, but instances of non-abstract
#  subclasses are.

class Numeric(Number):
    def __init__(self, value) -> None:
        self.value = value

    def __int__(self) -> int:
        exit(self.value)

num = Numeric(1)
assert is_scalar(num)
