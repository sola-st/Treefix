# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
# GH45263
d = {np.nan: [1, 2], None: [3, 4], NaT: [6, 7], True: [8, 9]}
df = DataFrame(data=d)
result = repr(df)
expected = """   NaN  None  NaT  True
0    1     3    6     8
1    2     4    7     9"""
assert result == expected
