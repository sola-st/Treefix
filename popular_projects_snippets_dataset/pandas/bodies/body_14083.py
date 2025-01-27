# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH 13998, GH 22505, # GH 49230
df = DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})

df_s = df.to_string(line_width=1, index=False)
expected = " x   \n 1  \\\n 2   \n 3   \n\n y  \n 4  \n 5  \n 6  "

assert df_s == expected

df = DataFrame({"x": [11, 22, 33], "y": [4, 5, 6]})

df_s = df.to_string(line_width=1, index=False)
expected = " x   \n11  \\\n22   \n33   \n\n y  \n 4  \n 5  \n 6  "

assert df_s == expected

df = DataFrame({"x": [11, 22, -33], "y": [4, 5, -6]})

df_s = df.to_string(line_width=1, index=False)
expected = "  x   \n 11  \\\n 22   \n-33   \n\n y  \n 4  \n 5  \n-6  "

assert df_s == expected
