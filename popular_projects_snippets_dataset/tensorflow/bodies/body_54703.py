# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
t = tensor_util.make_tensor_proto(10.0, shape=[1, 3])
self.assertProtoEquals("""
      dtype: DT_FLOAT
      tensor_shape { dim { size: 1 } dim { size: 3 } }
      float_val: 10.0
      """, t)
