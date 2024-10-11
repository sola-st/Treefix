# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
df = DataFrame({"\u05d0": [1, 2, 3], "\u05d1": [4, 5, 6], "c": [7, 8, 9]})
repr(df.columns)  # should not raise UnicodeDecodeError
