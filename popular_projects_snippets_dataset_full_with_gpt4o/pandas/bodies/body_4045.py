# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
if (opname in ("sum", "min", "max") and axis == 0) or opname in (
    "count",
    "nunique",
):
    getattr(float_string_frame, opname)(axis=axis)
else:
    msg = "|".join(
        [
            "Could not convert",
            "could not convert",
            "can't multiply sequence by non-int",
            "unsupported operand type",
            "not supported between instances of",
        ]
    )
    with pytest.raises(TypeError, match=msg):
        getattr(float_string_frame, opname)(axis=axis)
if opname != "nunique":
    getattr(float_string_frame, opname)(axis=axis, numeric_only=True)
