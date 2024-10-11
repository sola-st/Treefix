# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_copy.py
# GH#42477
df = DataFrame(
    {
        "a": np.random.randint(0, 100, size=55),
        "b": np.random.randint(0, 100, size=55),
    }
)

for i in range(0, 10):
    df.loc[:, f"n_{i}"] = np.random.randint(0, 100, size=55)

assert len(df._mgr.blocks) == 11
result = df.copy()
assert len(result._mgr.blocks) == 1
