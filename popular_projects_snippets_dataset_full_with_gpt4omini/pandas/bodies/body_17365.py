# Extracted from ./data/repos/pandas/pandas/tests/generic/test_label_or_level_utils.py
axis = frame._get_axis_number(axis)
for label in labels:
    df_dropped = frame._drop_labels_or_levels(label, axis=axis)

    if axis == 0:
        assert label in frame.columns
        assert label not in df_dropped.columns
    else:
        assert label in frame.index
        assert label not in df_dropped.index
