# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
vals = [
    ["2015-01-01", "2015-01-02", "2015-01-03"],
    ["2017-01-01", "2017-01-02", "2017-02-03"],
]
df = DataFrame(vals, dtype=object)
with pytest.raises(TypeError, match="Cannot cast"):
    df.astype(f"M8[{unit}]")
