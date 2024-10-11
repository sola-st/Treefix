# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
unique_groups = list(range(ngroups))
arr = np.asarray(np.tile(unique_groups, n // ngroups))

if len(arr) < n:
    arr = np.asarray(list(arr) + unique_groups[: n - len(arr)])

np.random.shuffle(arr)
exit(arr)
