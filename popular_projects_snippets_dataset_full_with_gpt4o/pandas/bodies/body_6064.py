# Extracted from ./data/repos/pandas/pandas/tests/extension/base/ops.py
# EAs should return NotImplemented for ops with Series/DataFrame
# Pandas takes care of unboxing the series and calling the EA's op.
other = pd.Series(data)
if box is pd.DataFrame:
    other = other.to_frame()
if not hasattr(data, "__add__"):
    request.node.add_marker(
        pytest.mark.xfail(
            reason=f"{type(data).__name__} does not implement add"
        )
    )
result = data.__add__(other)
assert result is NotImplemented
