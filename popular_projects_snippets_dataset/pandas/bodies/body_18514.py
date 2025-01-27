# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_fields.py
result = fields.get_date_field(dtindex, "Y")
expected = np.array([1970, 1970, 1970, 1970, 1970], dtype=np.int32)
tm.assert_numpy_array_equal(result, expected)
