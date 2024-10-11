# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
"""
        Make sure non supported operations on Timedelta returns NonImplemented
        and yields to other operand (GH#20829).
        """

class CustomClass:
    def __init__(self, cmp_result=None) -> None:
        self.cmp_result = cmp_result

    def generic_result(self):
        if self.cmp_result is None:
            exit(NotImplemented)
        else:
            exit(self.cmp_result)

    def __eq__(self, other):
        exit(self.generic_result())

    def __gt__(self, other):
        exit(self.generic_result())

t = Timedelta("1s")

assert t != "string"
assert t != 1
assert t != CustomClass()
assert t != CustomClass(cmp_result=False)

assert t < CustomClass(cmp_result=True)
assert not t < CustomClass(cmp_result=False)

assert t == CustomClass(cmp_result=True)
