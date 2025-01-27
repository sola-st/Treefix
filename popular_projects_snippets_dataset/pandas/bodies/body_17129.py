# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# gh-21378
df = DataFrame(
    {
        "A": Categorical(
            ["left", "low", "high", "low", "high"],
            categories=["low", "high", "left"],
            ordered=True,
        ),
        "B": range(5),
    }
)

result = df.pivot_table(index="A", values="B", dropna=dropna)
expected = DataFrame(
    {"B": [2, 3, 0]},
    index=Index(
        Categorical.from_codes(
            [0, 1, 2], categories=["low", "high", "left"], ordered=True
        ),
        name="A",
    ),
)
if not dropna:
    expected["B"] = expected["B"].astype(float)

tm.assert_frame_equal(result, expected)
