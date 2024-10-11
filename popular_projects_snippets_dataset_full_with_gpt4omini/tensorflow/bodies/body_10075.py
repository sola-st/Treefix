# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
x = np.array([[0, 0, 0], [0, 0, 0]], "float32")
self.assertAllClose(self.evaluate(math_ops.reduce_std(x)), 0)
self.assertAllClose(
    self.evaluate(math_ops.reduce_std(x, axis=0)), [0, 0, 0])

x = [[1, 2, 1, 1], [1, 1, 0, 1]]
with self.assertRaisesRegex(TypeError, "must be either real or complex"):
    math_ops.reduce_std(x)

x = [[1., 2., 1., 1.], [1., 1., 0., 1.]]
self.assertEqual(self.evaluate(math_ops.reduce_std(x)), 0.5)
x_np = np.array(x)
self.assertEqual(np.std(x_np), 0.5)
self.assertEqual(self.evaluate(math_ops.reduce_std(x_np)), 0.5)

x = ragged_factory_ops.constant([[5., 1., 4., 1.], [], [5., 9., 2.], [5.],
                                 []])
self.assertAllClose(math_ops.reduce_std(x, axis=0), [0., 4., 1., 0.])
