# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_sorting.py
c = Categorical([5, 3, 1, 4, 2], ordered=True)

expected = np.array([2, 4, 1, 3, 0])
tm.assert_numpy_array_equal(np.argsort(c), expected, check_dtype=False)

tm.assert_numpy_array_equal(
    np.argsort(c, kind="mergesort"), expected, check_dtype=False
)

msg = "the 'axis' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    np.argsort(c, axis=0)

msg = "the 'order' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    np.argsort(c, order="C")
