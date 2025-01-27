# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
td = Timedelta(1)

obj = constructor(td, dtype="m8[ns]")
assert get1(obj) == td
