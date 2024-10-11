# Extracted from ./data/repos/pandas/pandas/tests/generic/test_label_or_level_utils.py
axis = frame._get_axis_number(axis)
for level in levels:
    df_dropped = frame._drop_labels_or_levels(level, axis=axis)

    if axis == 0:
        assert level in frame.index.names
        assert level not in df_dropped.index.names
    else:
        assert level in frame.columns.names
        assert level not in df_dropped.columns.names
