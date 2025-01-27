# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
buf = StringIO()
float_frame.to_csv(buf)
buf.seek(0)
recons = read_csv(buf, index_col=0)
tm.assert_frame_equal(recons, float_frame)
