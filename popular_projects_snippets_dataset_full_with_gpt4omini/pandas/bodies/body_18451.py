# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#4532
# smoke tests for valid DateOffsets
ser = Series([Timestamp("20130101 9:01"), Timestamp("20130101 9:02")])
ser = tm.box_expected(ser, box_with_array)

offset_cls = getattr(pd.offsets, cls_name)
ser + offset_cls(5)
offset_cls(5) + ser
ser - offset_cls(5)
