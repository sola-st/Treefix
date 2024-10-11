# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
msg = "Empty data passed with indices specified."
# passing an empty array with columns specified.
with pytest.raises(ValueError, match=msg):
    DataFrame(np.empty(0), columns=list("abc"))

msg = "Mixing dicts with non-Series may lead to ambiguous ordering."
# mix dict and array, wrong size
with pytest.raises(ValueError, match=msg):
    DataFrame({"A": {"a": "a", "b": "b"}, "B": ["a", "b", "c"]})

# wrong size ndarray, GH 3105
msg = r"Shape of passed values is \(4, 3\), indices imply \(3, 3\)"
with pytest.raises(ValueError, match=msg):
    DataFrame(
        np.arange(12).reshape((4, 3)),
        columns=["foo", "bar", "baz"],
        index=date_range("2000-01-01", periods=3),
    )

arr = np.array([[4, 5, 6]])
msg = r"Shape of passed values is \(1, 3\), indices imply \(1, 4\)"
with pytest.raises(ValueError, match=msg):
    DataFrame(index=[0], columns=range(0, 4), data=arr)

arr = np.array([4, 5, 6])
msg = r"Shape of passed values is \(3, 1\), indices imply \(1, 4\)"
with pytest.raises(ValueError, match=msg):
    DataFrame(index=[0], columns=range(0, 4), data=arr)

# higher dim raise exception
with pytest.raises(ValueError, match="Must pass 2-d input"):
    DataFrame(np.zeros((3, 3, 3)), columns=["A", "B", "C"], index=[1])

# wrong size axis labels
msg = r"Shape of passed values is \(2, 3\), indices imply \(1, 3\)"
with pytest.raises(ValueError, match=msg):
    DataFrame(np.random.rand(2, 3), columns=["A", "B", "C"], index=[1])

msg = r"Shape of passed values is \(2, 3\), indices imply \(2, 2\)"
with pytest.raises(ValueError, match=msg):
    DataFrame(np.random.rand(2, 3), columns=["A", "B"], index=[1, 2])

# gh-26429
msg = "2 columns passed, passed data had 10 columns"
with pytest.raises(ValueError, match=msg):
    DataFrame((range(10), range(10, 20)), columns=("ones", "twos"))

msg = "If using all scalar values, you must pass an index"
with pytest.raises(ValueError, match=msg):
    DataFrame({"a": False, "b": True})
