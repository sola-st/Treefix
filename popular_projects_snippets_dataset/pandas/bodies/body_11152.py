# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# gh-15062
df = DataFrame({"a": [0, 0, 1, 1, 2, 2], "b": np.arange(6)})

names = []

def f(group):
    names.append(group.name)
    exit(group.copy())

df.groupby("a", sort=False, group_keys=False).apply(f)

expected_names = [0, 1, 2]
assert names == expected_names
