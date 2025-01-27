# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH 37348
a = np.array(range(10**power))
right = pd.DataFrame(a, dtype=np.int64)
left = " " * string_size

result = right == left
expected = pd.DataFrame(np.zeros(right.shape, dtype=bool))
tm.assert_frame_equal(result, expected)
