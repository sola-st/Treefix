# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
# GH 8215
# Make sure we return string for consistency with
# Series.to_csv()
csv_str = float_frame.to_csv(path_or_buf=None)
assert isinstance(csv_str, str)
recons = read_csv(StringIO(csv_str), index_col=0)
tm.assert_frame_equal(float_frame, recons)
