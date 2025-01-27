# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
# GH 15785
df = DataFrame(
    {"klass": range(5), "col": col, "attr1": [1, 0, 0, 0, 0], "attr2": col}
)
expected_value = pd.concat([pd.Series([1, 0, 0, 0, 0]), col], ignore_index=True)
result = melt(
    df, id_vars=["klass", "col"], var_name="attribute", value_name="value"
)
expected = DataFrame(
    {
        0: list(range(5)) * 2,
        1: pd.concat([col] * 2, ignore_index=True),
        2: ["attr1"] * 5 + ["attr2"] * 5,
        3: expected_value,
    }
)
expected.columns = ["klass", "col", "attribute", "value"]
tm.assert_frame_equal(result, expected)
