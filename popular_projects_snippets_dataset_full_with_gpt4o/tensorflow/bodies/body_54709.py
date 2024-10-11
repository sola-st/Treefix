# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
test_type = dtypes.float8_e5m2.as_numpy_dtype
t = tensor_util.make_tensor_proto(np.array([10.0, 20.0], dtype=test_type))
# 10.0: "I" = 73 = 10010 01: 2^(18 - 15) * (1 + 1/4)
# 20.0: "M" = 77 = 10011 01: 2^(19 - 15) * (1 + 1/4)
self.assertProtoEquals(
    """
      dtype: DT_FLOAT8_E5M2
      tensor_shape {
        dim {
          size: 2
        }
      }
      tensor_content: "IM"
      """, t)

a = tensor_util.MakeNdarray(t)
self.assertEqual(test_type, a.dtype)
self.assertAllClose(np.array([10.0, 20.0], dtype=test_type), a)
