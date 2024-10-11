# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
# GH 15348
expected = DataFrame(
    {
        "id1": df["id1"].tolist() * 2,
        "id2": df["id2"].tolist() * 2,
        "variable": ["A"] * 10 + ["B"] * 10,
        "value": (df["A"].tolist() + df["B"].tolist()),
    },
    columns=["id1", "id2", "variable", "value"],
)
result = df.melt(id_vars=["id1", "id2"], value_vars=type_(("A", "B")))
tm.assert_frame_equal(result, expected)
