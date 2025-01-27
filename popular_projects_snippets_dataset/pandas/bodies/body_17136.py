# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 7142 regression test
v = np.arange(5, dtype=np.float64)
df = DataFrame(
    {"float1": v, "float2": v + 2.0, "bool1": v <= 2, "bool2": v <= 3}
)

df_res = df.reset_index().pivot_table(
    index="index", columns=columns, values=values
)

result = dict(df_res.dtypes)
expected = {col: np.dtype("float64") for col in df_res}
assert result == expected
