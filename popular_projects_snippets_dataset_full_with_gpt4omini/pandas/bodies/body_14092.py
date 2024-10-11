# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
tm.reset_display_options()
df = DataFrame({"x": [3234, 0.253]})
df_s = df.to_string(justify="left")
expected = "   x       \n0  3234.000\n1     0.253"
assert df_s == expected
