# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_join.py
# https://github.com/pandas-dev/pandas/issues/19607
df1 = DataFrame({"a": [0, 10, 20]}, index=[1, 2, 3])
df2 = DataFrame({"b": [100, 200, 300]}, index=[4, 3, 2])
df3 = DataFrame({"c": [400, 500, 600]}, index=[2, 2, 4])

joined = df1.join([df2, df3], how="left")

expected = DataFrame(
    {
        "a": [0, 10, 10, 20],
        "b": [np.nan, 300, 300, 200],
        "c": [np.nan, 400, 500, np.nan],
    },
    index=[1, 2, 2, 3],
)

tm.assert_frame_equal(joined, expected)
