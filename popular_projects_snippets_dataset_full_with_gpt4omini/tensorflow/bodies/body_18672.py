# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
if shape is None:
    shape = [100]
t1 = self.evaluate(init(shape, dtype))
t2 = self.evaluate(init(shape, dtype))
self.assertEqual(tensor_shape.as_shape(shape), t1.shape)
self.assertEqual(tensor_shape.as_shape(shape), t2.shape)
self.assertFalse(np.allclose(t1, t2, rtol=1e-15, atol=1e-15))
