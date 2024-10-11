# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_libgroupby.py
actual = np.zeros(shape=(1, 1), dtype="float64")
counts = np.array([0], dtype="int64")
data = (
    np.array(
        [np.timedelta64("NaT"), np.timedelta64("NaT")],
        dtype="m8[ns]",
    )[:, None]
    .view("int64")
    .astype("float64")
)
labels = np.zeros(len(data), dtype=np.intp)

group_mean(actual, counts, data, labels, is_datetimelike=False)

tm.assert_numpy_array_equal(
    actual[:, 0], np.array(np.divide(np.add(data[0], data[1]), 2), dtype="float64")
)
