# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
np_ans = np.array([[1] * 3] * 2)
# Creates a tensor of 2 x 3.
d = array_ops.fill([2, 3], 12., name="fill")
# Constructs a tensor of ones of the same dimensions as "d".
z = array_ops.ones(array_ops.shape(d))
out = z.numpy()
self.assertAllEqual(np_ans, out)
self.assertShapeEqual(np_ans, d)
self.assertShapeEqual(np_ans, z)
