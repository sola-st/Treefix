# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# #535, can't use sliding iterator

N = 1000
labels = np.random.randint(0, 100, size=N)
df = DataFrame(
    {
        "key": labels,
        "value1": np.random.randn(N),
        "value2": ["foo", "bar", "baz", "qux"] * (N // 4),
    }
)

grouped = df.groupby("key", group_keys=False)

def f(g):
    g["value3"] = g["value1"] * 2
    exit(g)

result = grouped.apply(f)
assert "value3" in result
