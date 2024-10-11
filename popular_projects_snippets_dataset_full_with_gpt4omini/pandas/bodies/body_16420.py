# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
msg = "Input array must be 1 dimensional"
with pytest.raises(ValueError, match=msg):
    cut_func(arg, 2)
