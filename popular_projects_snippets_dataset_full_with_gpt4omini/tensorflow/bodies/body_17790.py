# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
# Shape x: [3, 4]
x = random_ops.random_uniform([3, 4])
elems = random_ops.random_uniform([6])
# Shape y: [6, 3, 4]
y = functional_ops.scan(lambda a, e: a + e, elems, initializer=x)
jacobian = gradients.jacobian(y, x)

expected_shape = [6, 3, 4, 3, 4]
self.assertAllEqual(expected_shape, jacobian.shape.as_list())
