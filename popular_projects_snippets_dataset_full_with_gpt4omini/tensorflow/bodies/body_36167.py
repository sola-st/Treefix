# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
elems = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
initializer = np.array(1.0)
# Multiply a * 1 each time
r = functional_ops.scan(lambda a, x: a * (x[0] + x[1]),
                        (elems + 1, -elems), initializer)
self.assertAllEqual([1.0, 1.0, 1.0, 1.0, 1.0, 1.0], self.evaluate(r))
