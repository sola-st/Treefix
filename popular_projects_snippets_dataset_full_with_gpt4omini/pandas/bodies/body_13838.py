# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
df = DataFrame([[0, 1], [2, 3]])

tslice_ = non_reducing_slice(slc)
assert isinstance(df.loc[tslice_], DataFrame)
