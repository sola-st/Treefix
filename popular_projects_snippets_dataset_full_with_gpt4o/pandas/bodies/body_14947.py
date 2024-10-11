# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_converter.py
data = ["2012-1-1", "2012-1-2"]
r1 = pc.convert([data, data], None, axis)
r2 = [pc.convert(data, None, axis) for _ in range(2)]
assert r1 == r2
