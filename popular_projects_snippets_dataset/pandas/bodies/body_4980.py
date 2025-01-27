# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# GH#42107
ser = Series([True, False, True, pd.NA], dtype="boolean")
result = ser.mode()
expected = Series({0: True}, dtype="boolean")
tm.assert_series_equal(result, expected)
