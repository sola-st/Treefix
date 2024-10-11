# Extracted from ./data/repos/tensorflow/tensorflow/python/dlpack/dlpack_test.py
tf_tensor = constant_op.constant([[1, 4], [5, 2]], dtype=dtypes.qint16)
_ = dlpack.to_dlpack(tf_tensor)
