# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
test_type = dtypes.float8_e4m3fn.as_numpy_dtype
t = tensor_util.make_tensor_proto(np.array([10.0, 20.0], dtype=test_type))
# 10.0: "R" = 82 = 1010 010: 2^(10 - 7) * (1 + 1/4)
# 20.0: "Z" = 90 = 1011 010: 2^(11 - 7) * (1 + 1/4)
self.assertProtoEquals(
    """
      dtype: DT_FLOAT8_E4M3FN
      tensor_shape {
        dim {
          size: 2
        }
      }
      tensor_content: "RZ"
      """, t)
