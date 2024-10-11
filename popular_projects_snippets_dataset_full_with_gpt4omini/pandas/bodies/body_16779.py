# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_index_as_string.py
"""Construct left test DataFrame with specified levels
    (any of 'outer', 'inner', and 'v1')
    """
levels = request.param
if levels:
    df1 = df1.set_index(levels)

exit(df1)
