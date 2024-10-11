# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_records.py
# xref issue: https://github.com/numpy/numpy/issues/2407
# Issue GH#11879. to_records used to raise an exception when used
# with column names containing non-ascii characters in Python 2
result = DataFrame(data={"accented_name_é": [1.0]}).to_records()

# Note that numpy allows for unicode field names but dtypes need
# to be specified using dictionary instead of list of tuples.
expected = np.rec.array(
    [(0, 1.0)],
    dtype={"names": ["index", "accented_name_é"], "formats": ["=i8", "=f8"]},
)
tm.assert_almost_equal(result, expected)
