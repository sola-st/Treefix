# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
# GH#39336
df = DataFrame(
    {
        "a": Series([0.123456789, 1.123456789], dtype="Float64"),
        "b": Series([1, 2], dtype="Int64"),
    }
)
result = df.to_string(formatters=["{:.2f}".format, "{:.2f}".format])
expected = """      a     b
0  0.12  1.00
1  1.12  2.00"""
assert result == expected
