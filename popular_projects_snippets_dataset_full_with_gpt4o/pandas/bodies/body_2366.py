# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_xs.py
obj = DataFrame({"A": [1, 2, 3]})
if frame_or_series is Series:
    obj = obj["A"]

msg = "Index must be a MultiIndex"
with pytest.raises(TypeError, match=msg):
    obj.xs(0, level="as")
