# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# gh-21133
df = DataFrame(
    {
        "A": Categorical(
            [np.nan, "low", "high", "low", "high"],
            categories=["low", "high"],
            ordered=True,
        ),
        "B": [0.0, 1.0, 2.0, 3.0, 4.0],
    }
)

result = df.pivot_table(index="A", values="B", dropna=dropna)
expected = DataFrame(
    {"B": [2.0, 3.0]},
    index=Index(
        Categorical.from_codes(
            [0, 1], categories=["low", "high"], ordered=True
        ),
        name="A",
    ),
)

tm.assert_frame_equal(result, expected)
