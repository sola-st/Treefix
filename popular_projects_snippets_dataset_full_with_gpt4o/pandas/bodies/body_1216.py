# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
obj = pd.PeriodIndex(["2011-01", "2011-02", "2011-03", "2011-04"], freq="M")
assert obj.dtype == "period[M]"

data = [
    pd.Period("2011-01", freq="M"),
    coerced_val,
    pd.Period("2011-02", freq="M"),
    pd.Period("2011-03", freq="M"),
    pd.Period("2011-04", freq="M"),
]
if isinstance(insert, pd.Period):
    exp = pd.PeriodIndex(data, freq="M")
    self._assert_insert_conversion(obj, insert, exp, coerced_dtype)

    # string that can be parsed to appropriate PeriodDtype
    self._assert_insert_conversion(obj, str(insert), exp, coerced_dtype)

else:
    result = obj.insert(0, insert)
    expected = obj.astype(object).insert(0, insert)
    tm.assert_index_equal(result, expected)

    # TODO: ATM inserting '2012-01-01 00:00:00' when we have obj.freq=="M"
    #  casts that string to Period[M], not clear that is desirable
    if not isinstance(insert, pd.Timestamp):
        # non-castable string
        result = obj.insert(0, str(insert))
        expected = obj.astype(object).insert(0, str(insert))
        tm.assert_index_equal(result, expected)
