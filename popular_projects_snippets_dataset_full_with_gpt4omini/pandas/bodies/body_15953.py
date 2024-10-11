# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_argsort.py
s = Series(np.random.randint(0, 100, size=10000))
mindexer = s.argsort(kind="mergesort")
qindexer = s.argsort()

mexpected = np.argsort(s.values, kind="mergesort")
qexpected = np.argsort(s.values, kind="quicksort")

tm.assert_series_equal(mindexer.astype(np.intp), Series(mexpected))
tm.assert_series_equal(qindexer.astype(np.intp), Series(qexpected))
msg = (
    r"ndarray Expected type <class 'numpy\.ndarray'>, "
    r"found <class 'pandas\.core\.series\.Series'> instead"
)
with pytest.raises(AssertionError, match=msg):
    tm.assert_numpy_array_equal(qindexer, mindexer)
