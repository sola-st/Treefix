# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_object.py
index = tm.makeStringIndex(100)
expected = pd.Index(index.values * 2)
tm.assert_index_equal(index + index, expected)
tm.assert_index_equal(index + index.tolist(), expected)
tm.assert_index_equal(index.tolist() + index, expected)

# test add and radd
index = pd.Index(list("abc"))
expected = pd.Index(["a1", "b1", "c1"])
tm.assert_index_equal(index + "1", expected)
expected = pd.Index(["1a", "1b", "1c"])
tm.assert_index_equal("1" + index, expected)
