# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
result3 = df.melt(id_vars=["id1", "id2"], value_vars="A")
assert len(result3) == 10

result4 = df.melt(id_vars=["id1", "id2"], value_vars=["A", "B"])
expected4 = DataFrame(
    {
        "id1": df["id1"].tolist() * 2,
        "id2": df["id2"].tolist() * 2,
        "variable": ["A"] * 10 + ["B"] * 10,
        "value": (df["A"].tolist() + df["B"].tolist()),
    },
    columns=["id1", "id2", "variable", "value"],
)
tm.assert_frame_equal(result4, expected4)
