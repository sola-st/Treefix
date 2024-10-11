# Extracted from ./data/repos/pandas/pandas/tests/extension/base/reshaping.py
# GH-20743
df1 = pd.DataFrame({"ext": data[:3], "int1": [1, 2, 3], "key": [0, 1, 2]})
df2 = pd.DataFrame({"int2": [1, 2, 3, 4], "key": [0, 0, 1, 3]})

res = pd.merge(df1, df2)
exp = pd.DataFrame(
    {
        "int1": [1, 1, 2],
        "int2": [1, 2, 3],
        "key": [0, 0, 1],
        "ext": data._from_sequence(
            [data[0], data[0], data[1]], dtype=data.dtype
        ),
    }
)
self.assert_frame_equal(res, exp[["ext", "int1", "key", "int2"]])

res = pd.merge(df1, df2, how="outer")
exp = pd.DataFrame(
    {
        "int1": [1, 1, 2, 3, np.nan],
        "int2": [1, 2, 3, np.nan, 4],
        "key": [0, 0, 1, 2, 3],
        "ext": data._from_sequence(
            [data[0], data[0], data[1], data[2], na_value], dtype=data.dtype
        ),
    }
)
self.assert_frame_equal(res, exp[["ext", "int1", "key", "int2"]])
