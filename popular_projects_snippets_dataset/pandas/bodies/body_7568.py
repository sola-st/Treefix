# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_conversion.py
tuples = [(1, "one"), (1, "two"), (2, "one"), (2, "two")]

index = MultiIndex.from_tuples(tuples)
result = index.to_frame(index=False)
expected = DataFrame(tuples)
tm.assert_frame_equal(result, expected)

result = index.to_frame()
expected.index = index
tm.assert_frame_equal(result, expected)

tuples = [(1, "one"), (1, "two"), (2, "one"), (2, "two")]
index = MultiIndex.from_tuples(tuples, names=["first", "second"])
result = index.to_frame(index=False)
expected = DataFrame(tuples)
expected.columns = ["first", "second"]
tm.assert_frame_equal(result, expected)

result = index.to_frame()
expected.index = index
tm.assert_frame_equal(result, expected)

# See GH-22580
index = MultiIndex.from_tuples(tuples)
result = index.to_frame(index=False, name=["first", "second"])
expected = DataFrame(tuples)
expected.columns = ["first", "second"]
tm.assert_frame_equal(result, expected)

result = index.to_frame(name=["first", "second"])
expected.index = index
expected.columns = ["first", "second"]
tm.assert_frame_equal(result, expected)

msg = "'name' must be a list / sequence of column names."
with pytest.raises(TypeError, match=msg):
    index.to_frame(name="first")

msg = "'name' should have same length as number of levels on index."
with pytest.raises(ValueError, match=msg):
    index.to_frame(name=["first"])

# Tests for datetime index
index = MultiIndex.from_product([range(5), pd.date_range("20130101", periods=3)])
result = index.to_frame(index=False)
expected = DataFrame(
    {
        0: np.repeat(np.arange(5, dtype="int64"), 3),
        1: np.tile(pd.date_range("20130101", periods=3), 5),
    }
)
tm.assert_frame_equal(result, expected)

result = index.to_frame()
expected.index = index
tm.assert_frame_equal(result, expected)

# See GH-22580
result = index.to_frame(index=False, name=["first", "second"])
expected = DataFrame(
    {
        "first": np.repeat(np.arange(5, dtype="int64"), 3),
        "second": np.tile(pd.date_range("20130101", periods=3), 5),
    }
)
tm.assert_frame_equal(result, expected)

result = index.to_frame(name=["first", "second"])
expected.index = index
tm.assert_frame_equal(result, expected)
