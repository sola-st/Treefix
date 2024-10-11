# Extracted from ./data/repos/tensorflow/tensorflow/python/dlpack/dlpack_test.py

def UnsupportedQint16():
    tf_tensor = constant_op.constant([[1, 4], [5, 2]], dtype=dtypes.qint16)
    _ = dlpack.to_dlpack(tf_tensor)

self.assertRaisesRegex(Exception, ".* is not supported by dlpack",
                       UnsupportedQint16)
