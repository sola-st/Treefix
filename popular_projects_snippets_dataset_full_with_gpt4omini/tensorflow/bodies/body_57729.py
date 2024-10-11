# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test_util.py
self.weight = constant_op.constant([[1e-3, -1e-3], [-2e-4, 2e-4]],
                                   shape=(2, 2),
                                   dtype=dtypes.float32)
self.bias = constant_op.constant([1.28, 2.55],
                                 shape=(2,),
                                 dtype=dtypes.float32)
