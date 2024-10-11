# Extracted from ./data/repos/pandas/pandas/tests/generic/test_label_or_level_utils.py

axis = df_levels._get_axis_number(axis)
# Compute expected labels and levels
expected_labels, expected_levels = get_labels_levels(df_levels)

# Transpose frame if axis == 1
if axis == 1:
    df_levels = df_levels.T

# Perform checks
assert_level_reference(df_levels, expected_levels, axis=axis)
assert_label_reference(df_levels, expected_labels, axis=axis)
