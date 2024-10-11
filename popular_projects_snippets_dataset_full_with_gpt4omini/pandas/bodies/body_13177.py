# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# #44847, #44914
# Not able to write float 16 column using pyarrow.
# Tests cleanup by pyarrow in case of an error
data = np.arange(2, 10, dtype=np.float16)
df = pd.DataFrame(data=data, columns=["fp16"])

with tm.ensure_clean() as path_str:
    path = path_type(path_str)
    with tm.external_error_raised(pyarrow.ArrowException):
        df.to_parquet(path=path, engine=pa)
    assert not os.path.isfile(path)
