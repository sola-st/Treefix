# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# Slicing
sl = float_frame[:20]
assert len(sl.index) == 20

# Column access
for _, series in sl.items():
    assert len(series.index) == 20
    assert tm.equalContents(series.index, sl.index)

for key, _ in float_frame._series.items():
    assert float_frame[key] is not None

assert "random" not in float_frame
with pytest.raises(KeyError, match="random"):
    float_frame["random"]
