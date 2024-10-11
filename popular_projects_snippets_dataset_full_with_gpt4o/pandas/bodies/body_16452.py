# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
df = DataFrame({"value": np.random.randint(0, 100, 20)})
labels = [f"{i} - {i + 9}" for i in range(0, 100, 10)]
with tm.assert_produces_warning(False):
    df["group"] = cut(df.value, range(0, 105, 10), right=False, labels=labels)
