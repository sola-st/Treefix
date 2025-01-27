# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_describe.py
df = DataFrame(
    {
        "string_data": ["a", "b", "c", "d", "e"],
        "bool_data": [True, True, False, False, False],
        "int_data": [10, 20, 30, 40, 50],
    }
)

# Integer data are included in .describe() output,
# Boolean and string data are not.
result = df.describe()
expected = DataFrame(
    {"int_data": [5, 30, df.int_data.std(), 10, 20, 30, 40, 50]},
    index=["count", "mean", "std", "min", "25%", "50%", "75%", "max"],
)
tm.assert_frame_equal(result, expected)

# Top value is a boolean value that is False
result = df.describe(include=["bool"])

expected = DataFrame(
    {"bool_data": [5, 2, False, 3]}, index=["count", "unique", "top", "freq"]
)
tm.assert_frame_equal(result, expected)
