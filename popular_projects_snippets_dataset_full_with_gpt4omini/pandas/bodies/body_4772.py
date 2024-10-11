# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
ser = Series([b"a", b"b", b"a\x9d"])

msg = (
    "'charmap' codec can't decode byte 0x9d in position 1: "
    "character maps to <undefined>"
)
with pytest.raises(UnicodeDecodeError, match=msg):
    ser.str.decode("cp1252")

result = ser.str.decode("cp1252", "ignore")
expected = ser.map(lambda x: x.decode("cp1252", "ignore"))
tm.assert_series_equal(result, expected)
