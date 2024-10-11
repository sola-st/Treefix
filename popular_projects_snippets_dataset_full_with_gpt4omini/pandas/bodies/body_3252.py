# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py

tf = mixed_float_frame.reindex(columns=["A", "B", "C"])

casted = tf.astype(np.int64)
casted = tf.astype(np.float32)  # noqa
