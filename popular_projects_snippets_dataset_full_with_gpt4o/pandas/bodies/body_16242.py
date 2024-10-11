# Extracted from ./data/repos/pandas/pandas/tests/series/test_logical_ops.py
# GH#4947
# logical ops should be label based

a = Series([True, False, True], list("bca"))
b = Series([False, True, False], list("abc"))

expected = Series([False, True, False], list("abc"))
result = a & b
tm.assert_series_equal(result, expected)

expected = Series([True, True, False], list("abc"))
result = a | b
tm.assert_series_equal(result, expected)

expected = Series([True, False, False], list("abc"))
result = a ^ b
tm.assert_series_equal(result, expected)

# rhs is bigger
a = Series([True, False, True], list("bca"))
b = Series([False, True, False, True], list("abcd"))

expected = Series([False, True, False, False], list("abcd"))
result = a & b
tm.assert_series_equal(result, expected)

expected = Series([True, True, False, False], list("abcd"))
result = a | b
tm.assert_series_equal(result, expected)

# filling

# vs empty
empty = Series([], dtype=object)

result = a & empty.copy()
expected = Series([False, False, False], list("bca"))
tm.assert_series_equal(result, expected)

result = a | empty.copy()
expected = Series([True, False, True], list("bca"))
tm.assert_series_equal(result, expected)

# vs non-matching
result = a & Series([1], ["z"])
expected = Series([False, False, False, False], list("abcz"))
tm.assert_series_equal(result, expected)

result = a | Series([1], ["z"])
expected = Series([True, True, False, False], list("abcz"))
tm.assert_series_equal(result, expected)

# identity
# we would like s[s|e] == s to hold for any e, whether empty or not
for e in [
    empty.copy(),
    Series([1], ["z"]),
    Series(np.nan, b.index),
    Series(np.nan, a.index),
]:
    result = a[a | e]
    tm.assert_series_equal(result, a[a])

for e in [Series(["z"])]:
    result = a[a | e]
    tm.assert_series_equal(result, a[a])

# vs scalars
index = list("bca")
t = Series([True, False, True])

for v in [True, 1, 2]:
    result = Series([True, False, True], index=index) | v
    expected = Series([True, True, True], index=index)
    tm.assert_series_equal(result, expected)

msg = "Cannot perform.+with a dtyped.+array and scalar of type"
for v in [np.nan, "foo"]:
    with pytest.raises(TypeError, match=msg):
        t | v

for v in [False, 0]:
    result = Series([True, False, True], index=index) | v
    expected = Series([True, False, True], index=index)
    tm.assert_series_equal(result, expected)

for v in [True, 1]:
    result = Series([True, False, True], index=index) & v
    expected = Series([True, False, True], index=index)
    tm.assert_series_equal(result, expected)

for v in [False, 0]:
    result = Series([True, False, True], index=index) & v
    expected = Series([False, False, False], index=index)
    tm.assert_series_equal(result, expected)
msg = "Cannot perform.+with a dtyped.+array and scalar of type"
for v in [np.nan]:
    with pytest.raises(TypeError, match=msg):
        t & v
