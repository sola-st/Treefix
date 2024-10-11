# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_index_as_string.py
"""Construct right test DataFrame with specified levels
    (any of 'outer', 'inner', and 'v2')
    """
levels = request.param

if levels:
    df2 = df2.set_index(levels)

exit(df2)
