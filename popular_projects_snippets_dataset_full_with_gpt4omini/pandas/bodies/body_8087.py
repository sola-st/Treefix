# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
values = index.tolist()[-2:] + ["nonexisting"]

expected = np.array([False, False, True, True])
tm.assert_numpy_array_equal(expected, index.isin(values, level=level))

index.name = "foobar"
tm.assert_numpy_array_equal(expected, index.isin(values, level="foobar"))
