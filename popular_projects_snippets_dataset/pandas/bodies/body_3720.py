# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_describe.py
# GH#11558
columns = pd.CategoricalIndex(["int1", "int2", "obj"], ordered=True, name="XXX")
df = DataFrame(
    {
        "int1": [10, 20, 30, 40, 50],
        "int2": [10, 20, 30, 40, 50],
        "obj": ["A", 0, None, "X", 1],
    },
    columns=columns,
)
result = df.describe()

exp_columns = pd.CategoricalIndex(
    ["int1", "int2"],
    categories=["int1", "int2", "obj"],
    ordered=True,
    name="XXX",
)
expected = DataFrame(
    {
        "int1": [5, 30, df.int1.std(), 10, 20, 30, 40, 50],
        "int2": [5, 30, df.int2.std(), 10, 20, 30, 40, 50],
    },
    index=["count", "mean", "std", "min", "25%", "50%", "75%", "max"],
    columns=exp_columns,
)

tm.assert_frame_equal(result, expected)
tm.assert_categorical_equal(result.columns.values, expected.columns.values)
