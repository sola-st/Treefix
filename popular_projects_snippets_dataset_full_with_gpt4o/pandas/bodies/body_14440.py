# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_select.py

# single dtypes
df = DataFrame(np.random.randn(10, 4), columns=["A", "A", "B", "B"])
df.index = date_range("20130101 9:30", periods=10, freq="T")

with ensure_clean_store(setup_path) as store:
    store.append("df", df)

    result = store.select("df")
    expected = df
    tm.assert_frame_equal(result, expected, by_blocks=True)

    result = store.select("df", columns=df.columns)
    expected = df
    tm.assert_frame_equal(result, expected, by_blocks=True)

    result = store.select("df", columns=["A"])
    expected = df.loc[:, ["A"]]
    tm.assert_frame_equal(result, expected)

# dups across dtypes
df = concat(
    [
        DataFrame(np.random.randn(10, 4), columns=["A", "A", "B", "B"]),
        DataFrame(
            np.random.randint(0, 10, size=20).reshape(10, 2), columns=["A", "C"]
        ),
    ],
    axis=1,
)
df.index = date_range("20130101 9:30", periods=10, freq="T")

with ensure_clean_store(setup_path) as store:
    store.append("df", df)

    result = store.select("df")
    expected = df
    tm.assert_frame_equal(result, expected, by_blocks=True)

    result = store.select("df", columns=df.columns)
    expected = df
    tm.assert_frame_equal(result, expected, by_blocks=True)

    expected = df.loc[:, ["A"]]
    result = store.select("df", columns=["A"])
    tm.assert_frame_equal(result, expected, by_blocks=True)

    expected = df.loc[:, ["B", "A"]]
    result = store.select("df", columns=["B", "A"])
    tm.assert_frame_equal(result, expected, by_blocks=True)

# duplicates on both index and columns
with ensure_clean_store(setup_path) as store:
    store.append("df", df)
    store.append("df", df)

    expected = df.loc[:, ["B", "A"]]
    expected = concat([expected, expected])
    result = store.select("df", columns=["B", "A"])
    tm.assert_frame_equal(result, expected, by_blocks=True)
