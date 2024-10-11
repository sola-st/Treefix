# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# Check that adding a "name" parameter to the copy is honored
# GH14302
index = Index([1, 2], name="MyName")
index1 = index.copy()

tm.assert_index_equal(index, index1)

index2 = index.copy(name="NewName")
tm.assert_index_equal(index, index2, check_names=False)
assert index.name == "MyName"
assert index2.name == "NewName"
