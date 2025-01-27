# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
# GH 24314
msg = "cannot specify integer `bins` when input data contains infinity"
with pytest.raises(ValueError, match=msg):
    cut(data, bins=3)
