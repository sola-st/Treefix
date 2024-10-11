# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
idx = numeric_idx
msg = "cannot perform __rmul__ with this index type"
with pytest.raises(TypeError, match=msg):
    idx * pd.date_range("20130101", periods=5)
