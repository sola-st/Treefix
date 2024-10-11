# Extracted from ./data/repos/pandas/pandas/tests/interchange/test_impl.py
df = pd.DataFrame(
    {
        "x": np.array([True, None, False, None, True]),
        "y": np.array([None, 2, None, 1, 2]),
        "z": np.array([9.2, 10.5, None, 11.8, None]),
    }
)

df2 = df.__dataframe__()

for col_name in df.columns:
    assert df2.get_column_by_name(col_name).null_count == 2
