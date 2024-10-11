# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py

# this is the only real reason to do it this way
tf = np.round(float_frame).astype(np.int32)
casted = tf.astype(np.float32, copy=False)

# TODO(wesm): verification?
tf = float_frame.astype(np.float64)
casted = tf.astype(np.int64, copy=False)  # noqa
