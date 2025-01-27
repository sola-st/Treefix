# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_diff.py
# mixed numeric
tf = datetime_frame.astype("float32")
the_diff = tf.diff(1)
tm.assert_series_equal(the_diff["A"], tf["A"] - tf["A"].shift(1))
