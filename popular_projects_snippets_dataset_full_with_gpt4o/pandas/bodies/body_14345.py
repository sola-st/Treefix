# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py
# GH 14435
idx = MultiIndex.from_arrays(
    [date_range("2000-01-01", periods=5), range(5)], names=["date", "id"]
)
df = DataFrame({"a": [1.1, 1.2, 1.3, 1.4, 1.5]}, index=idx)

with ensure_clean_store(setup_path) as store:
    store.append("df", df, data_columns=True)

    actual = store.select("df", where="id == 1")
    expected = df.iloc[[1], :]
    tm.assert_frame_equal(actual, expected)
