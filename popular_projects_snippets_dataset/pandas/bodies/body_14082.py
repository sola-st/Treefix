# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH 16839, GH 13032
df = DataFrame({"x": [11, 22], "y": [33, -44], "z": ["AAA", "   "]})

df_s = df.to_string(index=False)
# Leading space is expected for positive numbers.
expected = " x   y   z\n11  33 AAA\n22 -44    "
assert df_s == expected

df_s = df[["y", "x", "z"]].to_string(index=False)
expected = "  y  x   z\n 33 11 AAA\n-44 22    "
assert df_s == expected
