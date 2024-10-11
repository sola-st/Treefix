# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_categorical.py
# GH 25412
df1 = DataFrame({"f1": [1, 2, 3]})
df2 = DataFrame({"f1": [2, 3, 1], "f2": Series([4, 4, 4]).astype("category")})
result = pd.concat([df1, df2], sort=True)
dtype = CategoricalDtype([4])
expected = DataFrame(
    {
        "f1": [1, 2, 3, 2, 3, 1],
        "f2": Categorical.from_codes([-1, -1, -1, 0, 0, 0], dtype=dtype),
    },
    index=[0, 1, 2, 0, 1, 2],
)
tm.assert_frame_equal(result, expected)
