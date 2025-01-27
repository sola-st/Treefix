# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH 43321
df = DataFrame(
    {2010: [1], 2020: [3]},
    index=MultiIndex.from_product([["a"], ["b"]], names=["scen", "mod"]),
)

series = Series(
    [10.0, 20.0, 30.0],
    index=MultiIndex.from_product(
        [["a"], ["b"], [0, 1, 2]], names=["scen", "mod", "id"]
    ),
)

expected = DataFrame(
    {2010: [11.0, 21, 31.0], 2020: [13.0, 23.0, 33.0]},
    index=MultiIndex.from_product(
        [["a"], ["b"], [0, 1, 2]], names=["scen", "mod", "id"]
    ),
)
result = df.add(series, axis=0)

tm.assert_frame_equal(result, expected)
