# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 4928
# GH 21864
result = to_datetime([1, "1"], errors="ignore", cache=cache)

expected = Index(np.array([1, "1"], dtype="O"))
tm.assert_equal(result, expected)
msg = '^Given date string "1" not likely a datetime, at position 1$'
with pytest.raises(ValueError, match=msg):
    to_datetime([1, "1"], errors="raise", cache=cache)
