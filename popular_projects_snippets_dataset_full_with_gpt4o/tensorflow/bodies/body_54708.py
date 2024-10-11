# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
test_type = dtypes.bfloat16.as_numpy_dtype
t = tensor_util.make_tensor_proto(np.array([10.0, 20.0], dtype=test_type))
# 10.0: 16672 = 010000010(130) 0100000: (1+0/2+1/4) * 2^(130-127)
# 20.0: 16800 = 010000011(131) 0100000: (1+0/2+1/4) * 2^(131-127)
self.assertProtoEquals("""
      dtype: DT_BFLOAT16
      tensor_shape {
        dim {
          size: 2
        }
      }
      half_val: 16672
      half_val: 16800
      """, t)

a = tensor_util.MakeNdarray(t)
self.assertEqual(test_type, a.dtype)
self.assertAllClose(np.array([10.0, 20.0], dtype=test_type), a)
