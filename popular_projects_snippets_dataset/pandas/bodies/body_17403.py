# Extracted from ./data/repos/pandas/pandas/tests/interchange/test_impl.py
df = pd.DataFrame(
    {
        "x": np.array([1, 2, 3, 4, 0]),
        "y": np.array([1.5, 2.5, 3.5, 4.5, 0]),
        "z": np.array([True, False, True, True, True]),
    }
)

df2 = df.__dataframe__()

rng = np.random.RandomState(42)
dict_null = {col: rng.randint(low=0, high=len(df)) for col in df.columns}
for col, num_nulls in dict_null.items():
    null_idx = df.index[
        rng.choice(np.arange(len(df)), size=num_nulls, replace=False)
    ]
    df.loc[null_idx, col] = None

df2 = df.__dataframe__()

assert df2.get_column_by_name("x").null_count == dict_null["x"]
assert df2.get_column_by_name("y").null_count == dict_null["y"]
assert df2.get_column_by_name("z").null_count == dict_null["z"]
