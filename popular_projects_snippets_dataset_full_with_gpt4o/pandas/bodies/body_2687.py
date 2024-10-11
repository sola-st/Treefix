# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_dict_of_blocks.py
# GH#9607
df = DataFrame(float_frame, copy=True)
column = df.columns[0]

# use the default copy=True, change a column
blocks = df._to_dict_of_blocks(copy=True)
for _df in blocks.values():
    if column in _df:
        _df.loc[:, column] = _df[column] + 1

        # make sure we did not change the original DataFrame
assert not _df[column].equals(df[column])
