# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
elems = np.array([[1.0, 1.0, 1.0], [2.0, 3.0, 4.0]])
other_elems = np.array([-1.0, 1.0])
initializer = np.array([0.0, 0.0, 0.0])
r = functional_ops.foldl(lambda a, x: a + x[0] * x[1],
                         (elems, other_elems), initializer)
self.assertAllEqual([1.0, 2.0, 3.0], self.evaluate(r))
