# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_update.py
# GH 25807
result = DataFrame([pd.Timestamp("2019", tz="UTC")])
with tm.assert_produces_warning(None):
    result.update(result)
expected = DataFrame([pd.Timestamp("2019", tz="UTC")])
tm.assert_frame_equal(result, expected)
