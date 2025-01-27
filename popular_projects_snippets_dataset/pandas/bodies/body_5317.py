# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# GH#4731
per1 = Period(freq="D", year=2008, month=1, day=1)
per2 = Period(freq="D", year=2008, month=1, day=2)

msg = "|".join(
    [
        r"unsupported operand type\(s\)",
        "can only concatenate str",
        "must be str, not Period",
    ]
)
with pytest.raises(TypeError, match=msg):
    per1 + "str"
with pytest.raises(TypeError, match=msg):
    "str" + per1
with pytest.raises(TypeError, match=msg):
    per1 + per2
