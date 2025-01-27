# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_read_fwf.py
data = """ a    b    c
1    2    3.2
3    4    5.2
"""
colspecs = [(0, 5), (5, 10), (10, None)]
result = read_fwf(StringIO(data), colspecs=colspecs, dtype=dtype)

expected = DataFrame(
    {"a": [1, 3], "b": [2, 4], "c": [3.2, 5.2]}, columns=["a", "b", "c"]
)

for col, dt in dtype.items():
    expected[col] = expected[col].astype(dt)

tm.assert_frame_equal(result, expected)
