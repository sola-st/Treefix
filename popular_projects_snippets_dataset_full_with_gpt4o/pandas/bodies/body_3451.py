# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
# GH#3950
tz = tz_naive_fixture
idx1 = date_range("1/1/2011", periods=5, freq="D", tz=tz, name="idx1")
idx2 = Index(range(5), name="idx2", dtype="int64")
idx = MultiIndex.from_arrays([idx1, idx2])
df = DataFrame(
    {"a": np.arange(5, dtype="int64"), "b": ["A", "B", "C", "D", "E"]},
    index=idx,
)

expected = DataFrame(
    {
        "idx1": [
            datetime(2011, 1, 1),
            datetime(2011, 1, 2),
            datetime(2011, 1, 3),
            datetime(2011, 1, 4),
            datetime(2011, 1, 5),
        ],
        "idx2": np.arange(5, dtype="int64"),
        "a": np.arange(5, dtype="int64"),
        "b": ["A", "B", "C", "D", "E"],
    },
    columns=["idx1", "idx2", "a", "b"],
)
expected["idx1"] = expected["idx1"].apply(lambda d: Timestamp(d, tz=tz))

tm.assert_frame_equal(df.reset_index(), expected)

idx3 = date_range(
    "1/1/2012", periods=5, freq="MS", tz="Europe/Paris", name="idx3"
)
idx = MultiIndex.from_arrays([idx1, idx2, idx3])
df = DataFrame(
    {"a": np.arange(5, dtype="int64"), "b": ["A", "B", "C", "D", "E"]},
    index=idx,
)

expected = DataFrame(
    {
        "idx1": [
            datetime(2011, 1, 1),
            datetime(2011, 1, 2),
            datetime(2011, 1, 3),
            datetime(2011, 1, 4),
            datetime(2011, 1, 5),
        ],
        "idx2": np.arange(5, dtype="int64"),
        "idx3": [
            datetime(2012, 1, 1),
            datetime(2012, 2, 1),
            datetime(2012, 3, 1),
            datetime(2012, 4, 1),
            datetime(2012, 5, 1),
        ],
        "a": np.arange(5, dtype="int64"),
        "b": ["A", "B", "C", "D", "E"],
    },
    columns=["idx1", "idx2", "idx3", "a", "b"],
)
expected["idx1"] = expected["idx1"].apply(lambda d: Timestamp(d, tz=tz))
expected["idx3"] = expected["idx3"].apply(
    lambda d: Timestamp(d, tz="Europe/Paris")
)
tm.assert_frame_equal(df.reset_index(), expected)

# GH#7793
idx = MultiIndex.from_product(
    [["a", "b"], date_range("20130101", periods=3, tz=tz)]
)
df = DataFrame(
    np.arange(6, dtype="int64").reshape(6, 1), columns=["a"], index=idx
)

expected = DataFrame(
    {
        "level_0": "a a a b b b".split(),
        "level_1": [
            datetime(2013, 1, 1),
            datetime(2013, 1, 2),
            datetime(2013, 1, 3),
        ]
        * 2,
        "a": np.arange(6, dtype="int64"),
    },
    columns=["level_0", "level_1", "a"],
)
expected["level_1"] = expected["level_1"].apply(lambda d: Timestamp(d, tz=tz))
result = df.reset_index()
tm.assert_frame_equal(result, expected)
