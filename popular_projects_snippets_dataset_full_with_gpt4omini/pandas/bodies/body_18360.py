# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# don't allow division by NaT (maybe could in the future)
rng = timedelta_range("1 days", "10 days", name="foo")
rng = tm.box_expected(rng, box_with_array)

with pytest.raises(TypeError, match="unsupported operand type"):
    rng / NaT
with pytest.raises(TypeError, match="Cannot divide NaTType by"):
    NaT / rng

dt64nat = np.datetime64("NaT", "ns")
msg = "|".join(
    [
        # 'divide' on npdev as of 2021-12-18
        "ufunc '(true_divide|divide)' cannot use operands",
        "cannot perform __r?truediv__",
        "Cannot divide datetime64 by TimedeltaArray",
    ]
)
with pytest.raises(TypeError, match=msg):
    rng / dt64nat
with pytest.raises(TypeError, match=msg):
    dt64nat / rng
