# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
tm.assert_series_equal(float_frame.A, float_frame["A"])
msg = "'DataFrame' object has no attribute 'NONEXISTENT_NAME'"
with pytest.raises(AttributeError, match=msg):
    float_frame.NONEXISTENT_NAME
