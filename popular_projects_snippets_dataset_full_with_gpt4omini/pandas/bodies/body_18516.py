# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_fields.py
# treat dtindex as timedeltas for this next one
result = fields.get_timedelta_field(dtindex, "days")
expected = np.arange(5, dtype=np.int32) * 32
tm.assert_numpy_array_equal(result, expected)
