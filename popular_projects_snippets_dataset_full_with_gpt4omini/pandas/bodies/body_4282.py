# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
df = DataFrame(
    {2010: [1, 2, 3], 2020: [3, 4, 5]},
    index=MultiIndex.from_tuples(
        [
            ("a", "b", 0),
            ("a", "b", 1),
            ("a", "c", 2),
        ],
        names=["scen", "mod", "id"],
    ),
)

series = Series(
    [0.4],
    index=MultiIndex.from_product([["b"], ["a"]], names=["mod", "scen"]),
)

expected = DataFrame(
    {2010: [1.4, 2.4, np.nan], 2020: [3.4, 4.4, np.nan]},
    index=MultiIndex.from_tuples(
        [
            ("a", "b", 0),
            ("a", "b", 1),
            ("a", "c", 2),
        ],
        names=["scen", "mod", "id"],
    ),
)
result = df.add(series, axis=0)

tm.assert_frame_equal(result, expected)
