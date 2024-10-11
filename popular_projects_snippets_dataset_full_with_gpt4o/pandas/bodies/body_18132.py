# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# GH#23215
rng = period_range("1/1/2000", freq="D", periods=3)
rng = tm.box_expected(rng, box_with_array)

msg = "|".join(
    [
        r"(:?cannot add PeriodArray and .*)",
        r"(:?cannot subtract .* from (:?a\s)?.*)",
        r"(:?unsupported operand type\(s\) for \+: .* and .*)",
        r"unsupported operand type\(s\) for [+-]: .* and .*",
    ]
)
assert_invalid_addsub_type(rng, other, msg)
with pytest.raises(TypeError, match=msg):
    rng + other
with pytest.raises(TypeError, match=msg):
    other + rng
with pytest.raises(TypeError, match=msg):
    rng - other
with pytest.raises(TypeError, match=msg):
    other - rng
