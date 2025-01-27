# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_grad_test.py
x = array_ops.placeholder(dtypes.float32)
num_dimensions = array_ops.placeholder(dtypes.int32)
ret = random_grad.add_leading_unit_dimensions(x, num_dimensions)
with self.cached_session() as sess:
    ret_val = sess.run(ret, {x: np.ones([2, 2]), num_dimensions: 2})
self.assertAllEqual(ret_val.shape, [1, 1, 2, 2])
