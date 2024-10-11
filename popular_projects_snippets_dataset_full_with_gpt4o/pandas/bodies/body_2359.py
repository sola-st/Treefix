# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_xs.py
# see GH#6574
# missing values in returned index should be preserved
acc = [
    ("a", "abcde", 1),
    ("b", "bbcde", 2),
    ("y", "yzcde", 25),
    ("z", "xbcde", 24),
    ("z", None, 26),
    ("z", "zbcde", 25),
    ("z", "ybcde", 26),
]
df = DataFrame(acc, columns=["a1", "a2", "cnt"]).set_index(["a1", "a2"])
expected = DataFrame(
    {"cnt": [24, 26, 25, 26]},
    index=Index(["xbcde", np.nan, "zbcde", "ybcde"], name="a2"),
)

result = df.xs("z", level="a1")
tm.assert_frame_equal(result, expected)
