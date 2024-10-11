# Extracted from ./data/repos/pandas/pandas/tests/window/test_ewm.py
data = Series(range(1)).ewm(com=1, adjust=False)
with pytest.raises(NotImplementedError, match="sum is not"):
    data.sum()
