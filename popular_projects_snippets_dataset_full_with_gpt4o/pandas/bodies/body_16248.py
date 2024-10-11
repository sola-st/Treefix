# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH15520
msg = "not understood"
invalid_list = [Timestamp, "Timestamp", list]
for dtype in invalid_list:
    with pytest.raises(TypeError, match=msg):
        Series([], name="time", dtype=dtype)
