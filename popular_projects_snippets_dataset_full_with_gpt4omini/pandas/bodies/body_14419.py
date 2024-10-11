# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_complex.py
df = DataFrame(
    {"a": np.random.randn(100).astype(np.complex128), "b": np.random.randn(100)}
)

with ensure_clean_store(setup_path) as store:
    store.append("df", df, data_columns=["b"])
    store.append("df", df)
    result = store.select("df")
    tm.assert_frame_equal(pd.concat([df, df], axis=0), result)
