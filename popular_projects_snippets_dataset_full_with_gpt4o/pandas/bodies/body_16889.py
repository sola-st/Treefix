# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_qcut.py
with pytest.raises(ValueError, match="edges.*unique"):
    qcut([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 3)
