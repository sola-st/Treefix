# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_missing.py
# accept Categorical or ndarray value if it holds appropriate values
cat = Categorical(["A", "B", "C", None, None])

other = cat.fillna("C")
result = cat.fillna(other)
tm.assert_categorical_equal(result, other)
assert isna(cat[-1])  # didn't modify original inplace

other = np.array(["A", "B", "C", "B", "A"])
result = cat.fillna(other)
expected = Categorical(["A", "B", "C", "B", "A"], dtype=cat.dtype)
tm.assert_categorical_equal(result, expected)
assert isna(cat[-1])  # didn't modify original inplace
