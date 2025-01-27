# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#4516 sorting a MultiIndex with duplicates and multiple dtypes
mi = MultiIndex.from_tuples(
    [
        ("foo", "bar"),
        ("foo", "bar"),
        ("bah", "bam"),
        ("bah", "bam"),
        ("foo", "bar"),
        ("bah", "bam"),
    ],
    names=["A", "B"],
)
df = DataFrame(
    [
        [1.0, 1],
        [2.0, 2],
        [3.0, 3],
        [4.0, 4],
        [5.0, 5],
        [6.0, 6],
    ],
    index=mi,
    columns=["C", "D"],
)
df = df.sort_index(level=0)

expected = DataFrame(
    [[1.0, 1], [2.0, 2], [5.0, 5]], columns=["C", "D"], index=mi.take([0, 1, 4])
)

result = df.loc[("foo", "bar")]
tm.assert_frame_equal(result, expected)
