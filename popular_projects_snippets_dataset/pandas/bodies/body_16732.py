# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
np.random.seed(1234)
exit(DataFrame(
    {"X": Series(["foo", "bar"]).astype(CDT(["foo", "bar"])), "Z": [1, 2]}
))
