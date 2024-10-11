# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_converter.py
rs = pc.convert(["2012-1-1"], None, axis)[0]
xp = Period("2012-1-1").ordinal
assert rs == xp

rs = pc.convert("2012-1-1", None, axis)
assert rs == xp

rs = pc.convert([date(2012, 1, 1)], None, axis)[0]
assert rs == xp

rs = pc.convert(date(2012, 1, 1), None, axis)
assert rs == xp

rs = pc.convert([Timestamp("2012-1-1")], None, axis)[0]
assert rs == xp

rs = pc.convert(Timestamp("2012-1-1"), None, axis)
assert rs == xp

rs = pc.convert("2012-01-01", None, axis)
assert rs == xp

rs = pc.convert("2012-01-01 00:00:00+0000", None, axis)
assert rs == xp

rs = pc.convert(
    np.array(
        ["2012-01-01 00:00:00", "2012-01-02 00:00:00"],
        dtype="datetime64[ns]",
    ),
    None,
    axis,
)
assert rs[0] == xp
