# Extracted from ./data/repos/pandas/pandas/tests/generic/test_label_or_level_utils.py
for level in levels:
    assert frame._is_level_reference(level, axis=axis)
    assert not frame._is_label_reference(level, axis=axis)
    assert frame._is_label_or_level_reference(level, axis=axis)
