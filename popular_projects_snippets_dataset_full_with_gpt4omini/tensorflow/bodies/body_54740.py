# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util_test.py
t = tensor_util.make_tensor_proto([10.0, 20.0, np.array(30.0)])
a = tensor_util.MakeNdarray(t)
self.assertEqual(np.float32, a.dtype)
self.assertAllClose(np.array([10.0, 20.0, 30.0], dtype=np.float32), a)
