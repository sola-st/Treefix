# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike.py
index = simple_index

mask = np.ones(len(index), dtype=bool)
mask[-1] = False

result = index.where(mask, str(index[0]))
expected = index.where(mask, index[0])
tm.assert_index_equal(result, expected)

result = index.where(mask, [str(index[0])])
tm.assert_index_equal(result, expected)

expected = index.astype(object).where(mask, "foo")
result = index.where(mask, "foo")
tm.assert_index_equal(result, expected)

result = index.where(mask, ["foo"])
tm.assert_index_equal(result, expected)
