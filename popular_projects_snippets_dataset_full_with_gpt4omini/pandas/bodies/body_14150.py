# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
s = Series(range(10), dtype="float64")
res = s.to_string(float_format=lambda x: f"{x:2.1f}", max_rows=2)
exp = "0   0.0\n     ..\n9   9.0"
assert res == exp
