# Extracted from ./data/repos/pandas/pandas/tests/extension/base/io.py
df = pd.DataFrame({"with_dtype": pd.Series(data, dtype=str(data.dtype))})
csv_output = df.to_csv(index=False, na_rep=np.nan)
result = pd.read_csv(
    StringIO(csv_output), dtype={"with_dtype": str(data.dtype)}, engine=engine
)
expected = df
self.assert_frame_equal(result, expected)
