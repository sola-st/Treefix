# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
index1 = Index([1, 2, 3, 4, 5], name="index")
expected = Index([3, 4, 5])
result = index1.intersection(index2, sort)

if keeps_name:
    expected.name = "index"

assert result.name == expected.name
tm.assert_index_equal(result, expected)
