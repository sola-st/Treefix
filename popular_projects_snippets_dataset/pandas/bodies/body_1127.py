# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH 5286
tups = [
    ("Good Things", "C", np.nan),
    ("Good Things", "R", np.nan),
    ("Bad Things", "C", np.nan),
    ("Bad Things", "T", np.nan),
    ("Okay Things", "N", "B"),
    ("Okay Things", "N", "D"),
    ("Okay Things", "B", np.nan),
    ("Okay Things", "D", np.nan),
]
df = DataFrame(
    np.ones((8, 4)),
    columns=Index(["d1", "d2", "d3", "d4"]),
    index=MultiIndex.from_tuples(tups, names=["u1", "u2", "u3"]),
)
result = df.loc["Good Things"].loc["C"]
expected = DataFrame(
    np.ones((1, 4)),
    index=Index([np.nan], dtype="object", name="u3"),
    columns=Index(["d1", "d2", "d3", "d4"], dtype="object"),
)
tm.assert_frame_equal(result, expected)
