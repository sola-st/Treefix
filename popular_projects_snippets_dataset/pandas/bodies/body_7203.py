# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_setops.py
index1 = Index([5, 3, 2, 4, 1], name="index")
expected = Index([5, 3, 4])

if keeps_name:
    expected.name = "index"

result = index1.intersection(index2, sort=sort)
if sort is None:
    expected = expected.sort_values()
tm.assert_index_equal(result, expected)
