# Extracted from ./data/repos/pandas/pandas/tests/generic/test_label_or_level_utils.py
for label in labels:
    assert frame._is_label_reference(label, axis=axis)
    assert not frame._is_level_reference(label, axis=axis)
    assert frame._is_label_or_level_reference(label, axis=axis)
