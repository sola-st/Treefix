# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py

# GH 21625
df = DataFrame({"x": [0.19999]})
expected = "      x\n0 0.200"
assert df.to_string(float_format="%.3f") == expected

# GH 22270
df = DataFrame({"x": [100.0]})
expected = "    x\n0 100"
assert df.to_string(float_format="%.0f") == expected
