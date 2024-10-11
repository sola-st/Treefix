# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_drop.py
dropped = idx.drop([("foo", "two"), ("qux", "one")])

index = MultiIndex.from_tuples([("foo", "two"), ("qux", "one")])
dropped2 = idx.drop(index)

expected = idx[[0, 2, 3, 5]]
tm.assert_index_equal(dropped, expected)
tm.assert_index_equal(dropped2, expected)

dropped = idx.drop(["bar"])
expected = idx[[0, 1, 3, 4, 5]]
tm.assert_index_equal(dropped, expected)

dropped = idx.drop("foo")
expected = idx[[2, 3, 4, 5]]
tm.assert_index_equal(dropped, expected)

index = MultiIndex.from_tuples([("bar", "two")])
with pytest.raises(KeyError, match=r"^15$"):
    idx.drop([("bar", "two")])
with pytest.raises(KeyError, match=r"^15$"):
    idx.drop(index)
with pytest.raises(KeyError, match=r"^'two'$"):
    idx.drop(["foo", "two"])

# partially correct argument
mixed_index = MultiIndex.from_tuples([("qux", "one"), ("bar", "two")])
with pytest.raises(KeyError, match=r"^15$"):
    idx.drop(mixed_index)

# error='ignore'
dropped = idx.drop(index, errors="ignore")
expected = idx[[0, 1, 2, 3, 4, 5]]
tm.assert_index_equal(dropped, expected)

dropped = idx.drop(mixed_index, errors="ignore")
expected = idx[[0, 1, 2, 3, 5]]
tm.assert_index_equal(dropped, expected)

dropped = idx.drop(["foo", "two"], errors="ignore")
expected = idx[[2, 3, 4, 5]]
tm.assert_index_equal(dropped, expected)

# mixed partial / full drop
dropped = idx.drop(["foo", ("qux", "one")])
expected = idx[[2, 3, 5]]
tm.assert_index_equal(dropped, expected)

# mixed partial / full drop / error='ignore'
mixed_index = ["foo", ("qux", "one"), "two"]
with pytest.raises(KeyError, match=r"^'two'$"):
    idx.drop(mixed_index)
dropped = idx.drop(mixed_index, errors="ignore")
expected = idx[[2, 3, 5]]
tm.assert_index_equal(dropped, expected)
