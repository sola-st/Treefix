# Extracted from ./data/repos/pandas/pandas/tests/extension/base/ops.py
# EAs should return NotImplemented for ops with Series/DataFrame
# Pandas takes care of unboxing the series and calling the EA's op.
other = pd.Series(data)
if box is pd.DataFrame:
    other = other.to_frame()

if hasattr(data, "__eq__"):
    result = data.__eq__(other)
    assert result is NotImplemented
else:
    pytest.skip(f"{type(data).__name__} does not implement __eq__")

if hasattr(data, "__ne__"):
    result = data.__ne__(other)
    assert result is NotImplemented
else:
    pytest.skip(f"{type(data).__name__} does not implement __ne__")
