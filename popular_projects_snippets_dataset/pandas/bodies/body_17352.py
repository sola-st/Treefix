# Extracted from ./data/repos/pandas/pandas/tests/generic/test_label_or_level_utils.py

axis = df_ambig._get_axis_number(axis)

# Transpose frame if axis == 1
if axis == 1:
    df_ambig = df_ambig.T

# df has both an on-axis level and off-axis label named L1
# Therefore L1 should reference the label, not the level
assert_label_reference(df_ambig, ["L1"], axis=axis)

# df has an on-axis level named L2 and it is not ambiguous
# Therefore L2 is an level reference
assert_level_reference(df_ambig, ["L2"], axis=axis)

# df has a column named L3 and it not an level reference
assert_label_reference(df_ambig, ["L3"], axis=axis)
