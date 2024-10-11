# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_fields.py
# https://github.com/vaexio/vaex/issues/357
#  fields functions shouldn't raise when we pass read-only data
result = fields.get_date_name_field(dtindex, "month_name")
expected = np.array(["January", "February", "March", "April", "May"], dtype=object)
tm.assert_numpy_array_equal(result, expected)
