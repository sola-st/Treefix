# Extracted from ./data/repos/pandas/pandas/tests/series/test_ufunc.py
box = box_with_array
values = values_for_np_reduce

same_type = True
if box is pd.Index and values.dtype.kind in ["i", "f"]:
    # ATM Index casts to object, so we get python ints/floats
    same_type = False

with tm.assert_produces_warning(None):
    obj = box(values)

result = np.minimum.reduce(obj)
if box is pd.DataFrame:
    expected = obj.min(numeric_only=False)
    tm.assert_series_equal(result, expected)
else:
    expected = values[0]
    assert result == expected
    if same_type:
        # check we have e.g. Timestamp instead of dt64
        assert type(result) == type(expected)
