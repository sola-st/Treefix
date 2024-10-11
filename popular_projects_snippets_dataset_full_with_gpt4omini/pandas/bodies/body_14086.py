# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
df = DataFrame({"a": [1.5, 1e-17, -5.5e-7]})

result = df.to_string()
# sadness per above
if _three_digit_exp():
    expected = (
        "               a\n"
        "0  1.500000e+000\n"
        "1  1.000000e-017\n"
        "2 -5.500000e-007"
    )
else:
    expected = (
        "              a\n"
        "0  1.500000e+00\n"
        "1  1.000000e-17\n"
        "2 -5.500000e-07"
    )
assert result == expected

# but not all exactly zero
df = df * 0
result = df.to_string()
expected = "   0\n0  0\n1  0\n2 -0"
