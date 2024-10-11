# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
if exception_type is not None:
    with pytest.raises(exception_type, match=tm.EMPTY_STRING_PATTERN):
        json_normalize(data, record_path=record_path)
else:
    result = json_normalize(data, record_path=record_path)
    expected = DataFrame([0, 1], columns=["a"])
    tm.assert_frame_equal(result, expected)
