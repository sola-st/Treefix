# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
# GH#41828
df1 = data.copy()
df1.attrs = {1: 1}
df2 = data.copy()
df2.attrs = {1: 2}
df = concat([df1, df2])
assert len(df.attrs) == 0
