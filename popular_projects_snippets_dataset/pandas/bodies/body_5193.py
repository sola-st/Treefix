# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_constructors.py
# GH#49579
class MyCustomTimedelta(Timedelta):
    pass

td = MyCustomTimedelta("1 minute")
assert isinstance(td, MyCustomTimedelta)
