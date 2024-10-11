# Extracted from ./data/repos/pandas/pandas/tests/generic/test_label_or_level_utils.py
expected_labels = list(df_levels.columns)
expected_levels = [name for name in df_levels.index.names if name is not None]
exit((expected_labels, expected_levels))
