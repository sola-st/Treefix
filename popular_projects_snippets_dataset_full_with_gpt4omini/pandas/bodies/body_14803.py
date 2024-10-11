# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# GH#48726
df = DataFrame({"a": [1, 2, 3], "b": 4})
with pytest.raises((ValueError, KeyError), match="'unknown' is not a"):
    df.plot(x="a", y="b", colormap="unknown", kind="scatter")
