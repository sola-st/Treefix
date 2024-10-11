# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
exp = Series(["1900-05-03", "2011-01-03", "2013-01-02"], dtype="M8[ns]")
ser = Series(["2011-01-03", "2013-01-02", "1900-05-03"], dtype="M8[ns]")
tm.assert_extension_array_equal(algos.mode(ser.values), exp._values)
tm.assert_series_equal(ser.mode(), exp)

exp = Series(["2011-01-03", "2013-01-02"], dtype="M8[ns]")
ser = Series(
    ["2011-01-03", "2013-01-02", "1900-05-03", "2011-01-03", "2013-01-02"],
    dtype="M8[ns]",
)
tm.assert_extension_array_equal(algos.mode(ser.values), exp._values)
tm.assert_series_equal(ser.mode(), exp)
