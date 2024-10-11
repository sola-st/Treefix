# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# GH#17983
ts = Timestamp("2017")
per = Period("2017", freq="M")

# We may get a different message depending on which class raises
# the error.
msg = "|".join(
    [
        "cannot add",
        "unsupported operand",
        "can only operate on a",
        "incompatible type",
        "ufunc add cannot use operands",
    ]
)
with pytest.raises(TypeError, match=msg):
    lbox(ts) + rbox(per)

with pytest.raises(TypeError, match=msg):
    lbox(per) + rbox(ts)

with pytest.raises(TypeError, match=msg):
    lbox(per) + rbox(per)
