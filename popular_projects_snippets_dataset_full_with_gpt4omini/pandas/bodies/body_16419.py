# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
with pytest.raises(ValueError, match=msg):
    cut(x, bins)
