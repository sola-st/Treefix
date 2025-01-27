# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# see gh-14827
df = DataFrame(
    {
        "a": [1.2, decimal.Decimal(3.14), decimal.Decimal("infinity"), "0.1"],
        "b": [1.0, 2.0, 3.0, 4.0],
    }
)

expected = DataFrame({"a": [1.2, 3.14, np.inf, 0.1], "b": [1.0, 2.0, 3.0, 4.0]})

df_copy = df.copy()
df_copy[columns] = df_copy[columns].apply(to_numeric)

tm.assert_frame_equal(df_copy, expected)
