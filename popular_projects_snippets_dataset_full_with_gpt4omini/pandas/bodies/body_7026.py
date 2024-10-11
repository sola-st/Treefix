# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_indexing.py
np.random.seed(123456789)

ci = CategoricalIndex(list("aabbca"), categories=list("cab"), ordered=False)
oidx = Index(np.array(ci))

msg = "Reindexing only valid with uniquely valued Index objects"

for n in [1, 2, 5, len(ci)]:
    finder = oidx[np.random.randint(0, len(ci), size=n)]

    with pytest.raises(InvalidIndexError, match=msg):
        ci.get_indexer(finder)

        # see gh-17323
        #
        # Even when indexer is equal to the
        # members in the index, we should
        # respect duplicates instead of taking
        # the fast-track path.
for finder in [list("aabbca"), list("aababca")]:

    with pytest.raises(InvalidIndexError, match=msg):
        ci.get_indexer(finder)
