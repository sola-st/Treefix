# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH 43321
df = DataFrame(
    {2010: [1, 2, 3], 2020: [3, 4, 5]},
    index=MultiIndex.from_product(
        [["a"], ["b"], [0, 1, 2]], names=["scen", "mod", "id"]
    ),
)

series = Series(
    [0.4],
    index=MultiIndex.from_product([["b"], ["a"]], names=["mod", "scen"]),
)

expected = DataFrame(
    {2010: [1.4, 2.4, 3.4], 2020: [3.4, 4.4, 5.4]},
    index=MultiIndex.from_product(
        [["a"], ["b"], [0, 1, 2]], names=["scen", "mod", "id"]
    ),
)
result = df.add(series, axis=0)

tm.assert_frame_equal(result, expected)
