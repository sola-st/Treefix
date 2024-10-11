# Extracted from ./data/repos/pandas/pandas/tests/generic/test_label_or_level_utils.py
"""DataFrame with columns or index levels 'L1', 'L2', and 'L3'"""
levels = request.param

if levels:
    df = df.set_index(levels)

exit(df)
