# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_records.py
arr = np.array(
    [(1.0, 1.0, 2, 2), (3.0, 3.0, 4, 4), (5.0, 5.0, 6, 6), (7.0, 7.0, 8, 8)],
    dtype=[
        ("x", np.float64),
        ("u", np.float32),
        ("y", np.int64),
        ("z", np.int32),
    ],
)
df = DataFrame.from_records(iter(arr), nrows=2)
xp = DataFrame(
    {
        "x": np.array([1.0, 3.0], dtype=np.float64),
        "u": np.array([1.0, 3.0], dtype=np.float32),
        "y": np.array([2, 4], dtype=np.int64),
        "z": np.array([2, 4], dtype=np.int32),
    }
)
tm.assert_frame_equal(df.reindex_like(xp), xp)

# no dtypes specified here, so just compare with the default
arr = [(1.0, 2), (3.0, 4), (5.0, 6), (7.0, 8)]
df = DataFrame.from_records(iter(arr), columns=["x", "y"], nrows=2)
tm.assert_frame_equal(df, xp.reindex(columns=["x", "y"]), check_dtype=False)
