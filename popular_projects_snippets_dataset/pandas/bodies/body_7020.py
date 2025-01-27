# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_indexing.py
# GH 12531
cidx1 = CategoricalIndex(list("abcde"), categories=list("edabc"))
idx1 = Index(list("abcde"))
assert cidx1.get_loc("a") == idx1.get_loc("a")
assert cidx1.get_loc("e") == idx1.get_loc("e")

for i in [cidx1, idx1]:
    with pytest.raises(KeyError, match="'NOT-EXIST'"):
        i.get_loc("NOT-EXIST")

        # non-unique
cidx2 = CategoricalIndex(list("aacded"), categories=list("edabc"))
idx2 = Index(list("aacded"))

# results in bool array
res = cidx2.get_loc("d")
tm.assert_numpy_array_equal(res, idx2.get_loc("d"))
tm.assert_numpy_array_equal(
    res, np.array([False, False, False, True, False, True])
)
# unique element results in scalar
res = cidx2.get_loc("e")
assert res == idx2.get_loc("e")
assert res == 4

for i in [cidx2, idx2]:
    with pytest.raises(KeyError, match="'NOT-EXIST'"):
        i.get_loc("NOT-EXIST")

        # non-unique, sliceable
cidx3 = CategoricalIndex(list("aabbb"), categories=list("abc"))
idx3 = Index(list("aabbb"))

# results in slice
res = cidx3.get_loc("a")
assert res == idx3.get_loc("a")
assert res == slice(0, 2, None)

res = cidx3.get_loc("b")
assert res == idx3.get_loc("b")
assert res == slice(2, 5, None)

for i in [cidx3, idx3]:
    with pytest.raises(KeyError, match="'c'"):
        i.get_loc("c")
