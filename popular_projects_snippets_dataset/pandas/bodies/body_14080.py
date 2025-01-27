# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
df = DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})

df_s = df.to_string(header=False)
expected = "0  1  4\n1  2  5\n2  3  6"

assert df_s == expected
