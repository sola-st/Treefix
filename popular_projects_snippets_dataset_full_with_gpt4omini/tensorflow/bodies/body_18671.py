# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
if shape is None:
    shape = [100]
t1 = self.evaluate(init1(shape, dtype))
t2 = self.evaluate(init2(shape, dtype))
self.assertEqual(tensor_shape.as_shape(shape), t1.shape)
self.assertEqual(tensor_shape.as_shape(shape), t2.shape)
self.assertEqual(assertion, np.allclose(t1, t2, rtol=1e-15, atol=1e-15))
