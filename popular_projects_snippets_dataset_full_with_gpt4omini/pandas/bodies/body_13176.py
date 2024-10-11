# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# #44847, #44914
# Not able to write float 16 column using pyarrow.
data = np.arange(2, 10, dtype=np.float16)
df = pd.DataFrame(data=data, columns=["fp16"])
self.check_external_error_on_write(df, pa, pyarrow.ArrowException)
