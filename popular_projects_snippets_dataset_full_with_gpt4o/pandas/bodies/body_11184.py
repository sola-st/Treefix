# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH 18451
df = DataFrame([{"a": 1, "b": 2, "c": 99}, {"a": 1, "b": 2, "c": 88}])
df = df.set_index(["a", "b"])

grp = df.groupby(["a", "b"])
result = grp.indices
expected = {(1, 2): np.array([0, 1], dtype=np.int64)}

assert len(result) == 1
key = (1, 2)
assert (result[key] == expected[key]).all()
