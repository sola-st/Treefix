# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_stitch_op_test.py
indices = [
    constant_op.constant(6),
    constant_op.constant([4, 1]),
    constant_op.constant([[5, 2], [0, 3]])
]
data = [
    constant_op.constant([61., 62.]),
    constant_op.constant([[41., 42.], [11., 12.]]),
    constant_op.constant([[[51., 52.], [21., 22.]],
                          [[1., 2.], [31., 32.]]])
]
stitched_t = self.stitch_op(indices, data)
stitched_val = self.evaluate(stitched_t)
correct = 10. * np.arange(7)[:, None] + [1., 2.]
self.assertAllEqual(correct, stitched_val)
self.assertEqual([7, 2], stitched_t.get_shape().as_list())
# Test gradients
stitched_grad = 7. * stitched_val
grads = gradients_impl.gradients(stitched_t, indices + data,
                                 stitched_grad)
self.assertEqual(grads[:3], [None] * 3)  # Indices have no gradients
for datum, grad in zip(data, self.evaluate(grads[3:])):
    self.assertAllEqual(7. * self.evaluate(datum), grad)
