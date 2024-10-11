# Extracted from ./data/repos/pandas/pandas/tests/generic/test_label_or_level_utils.py

# Compute expected labels and levels
expected_labels, expected_levels = get_labels_levels(df_levels)

axis = df_levels._get_axis_number(axis)
# Transpose frame if axis == 1
if axis == 1:
    df_levels = df_levels.T

# Perform checks
assert_labels_dropped(df_levels, expected_labels, axis=axis)
assert_levels_dropped(df_levels, expected_levels, axis=axis)

with pytest.raises(ValueError, match="not valid labels or levels"):
    df_levels._drop_labels_or_levels("L4", axis=axis)
