# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_dict_of_blocks.py
# GH#9607
df = DataFrame(float_frame, copy=True)
column = df.columns[0]

# use the copy=False, change a column
blocks = df._to_dict_of_blocks(copy=False)
for _df in blocks.values():
    if column in _df:
        _df.loc[:, column] = _df[column] + 1

if not using_copy_on_write:
    # make sure we did change the original DataFrame
    assert _df[column].equals(df[column])
else:
    assert not _df[column].equals(df[column])
