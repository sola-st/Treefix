# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# GH#4521
# divide/multiply by integers

tdser = Series(["59 Days", "59 Days", "NaT"], dtype="m8[ns]")
vector = vector.astype(any_real_numpy_dtype)

expected = Series(["2.95D", "1D 23H 12m", "NaT"], dtype="timedelta64[ns]")

tdser = tm.box_expected(tdser, box_with_array)
xbox = get_upcast_box(tdser, vector)
expected = tm.box_expected(expected, xbox)

result = tdser / vector
tm.assert_equal(result, expected)

pattern = "|".join(
    [
        "true_divide'? cannot use operands",
        "cannot perform __div__",
        "cannot perform __truediv__",
        "unsupported operand",
        "Cannot divide",
        "ufunc 'divide' cannot use operands with types",
    ]
)
with pytest.raises(TypeError, match=pattern):
    vector / tdser

result = tdser / vector.astype(object)
if box_with_array is DataFrame:
    expected = [tdser.iloc[0, n] / vector[n] for n in range(len(vector))]
    expected = tm.box_expected(expected, xbox).astype(object)
else:
    expected = [tdser[n] / vector[n] for n in range(len(tdser))]
    expected = [
        x if x is not NaT else np.timedelta64("NaT", "ns") for x in expected
    ]
    if xbox is tm.to_array:
        expected = tm.to_array(expected).astype(object)
    else:
        expected = xbox(expected, dtype=object)

tm.assert_equal(result, expected)

with pytest.raises(TypeError, match=pattern):
    vector.astype(object) / tdser
