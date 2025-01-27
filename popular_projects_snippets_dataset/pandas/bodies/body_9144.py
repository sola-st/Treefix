# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_dtypes.py

# test dtype comparisons between cats

c1 = Categorical(list("aabca"), categories=list("abc"), ordered=False)
c2 = Categorical(list("aabca"), categories=list("cab"), ordered=False)
c3 = Categorical(list("aabca"), categories=list("cab"), ordered=True)
assert c1._categories_match_up_to_permutation(c1)
assert c2._categories_match_up_to_permutation(c2)
assert c3._categories_match_up_to_permutation(c3)
assert c1._categories_match_up_to_permutation(c2)
assert not c1._categories_match_up_to_permutation(c3)
assert not c1._categories_match_up_to_permutation(Index(list("aabca")))
assert not c1._categories_match_up_to_permutation(c1.astype(object))
assert c1._categories_match_up_to_permutation(CategoricalIndex(c1))
assert c1._categories_match_up_to_permutation(
    CategoricalIndex(c1, categories=list("cab"))
)
assert not c1._categories_match_up_to_permutation(
    CategoricalIndex(c1, ordered=True)
)

# GH 16659
s1 = Series(c1)
s2 = Series(c2)
s3 = Series(c3)
assert c1._categories_match_up_to_permutation(s1)
assert c2._categories_match_up_to_permutation(s2)
assert c3._categories_match_up_to_permutation(s3)
assert c1._categories_match_up_to_permutation(s2)
assert not c1._categories_match_up_to_permutation(s3)
assert not c1._categories_match_up_to_permutation(s1.astype(object))
