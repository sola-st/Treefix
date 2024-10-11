# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 20909
mdf = DataFrame(
    {
        "A": [1, 2, 3],
        "B": [1.0, 2.0, 3.0],
        "C": ["foo", "bar", "baz"],
        "D": date_range("20130101", periods=3),
    }
)

# sorted index
msg = "does not support reduction"
with pytest.raises(TypeError, match=msg):
    mdf.agg(["min", "sum"])

with pytest.raises(TypeError, match=msg):
    mdf[["D", "C", "B", "A"]].agg(["sum", "min"])
