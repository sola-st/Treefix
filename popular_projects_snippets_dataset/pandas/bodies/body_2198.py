# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
malformed = np.array(["1/100/2000", np.nan], dtype=object)

# GH 10636, default is now 'raise'
msg = r"Unknown datetime string format"
with pytest.raises(ValueError, match=msg):
    with tm.assert_produces_warning(
        UserWarning, match="Could not infer format"
    ):
        to_datetime(malformed, errors="raise", cache=cache)

with tm.assert_produces_warning(UserWarning, match="Could not infer format"):
    result = to_datetime(malformed, errors="ignore", cache=cache)
# GH 21864
expected = Index(malformed)
tm.assert_index_equal(result, expected)

with pytest.raises(ValueError, match=msg):
    with tm.assert_produces_warning(
        UserWarning, match="Could not infer format"
    ):
        to_datetime(malformed, errors="raise", cache=cache)
