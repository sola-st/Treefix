# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_reshape.py
index = Index(["a", "b", "c", "d", "e", "f"])

foos = [index[:2], index[2:4], index[4:]]
result = foos[0].append(foos[1:])
tm.assert_index_equal(result, index)

# empty
result = index.append([])
tm.assert_index_equal(result, index)
