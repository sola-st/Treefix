# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
elems = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
initializer = (np.array(1.0), np.array(-1.0))
r = functional_ops.scan(lambda a, x: (a[0] * x, -a[1] * x), elems,
                        initializer)
r_value = self.evaluate(r)

self.assertAllEqual([1.0, 2.0, 6.0, 24.0, 120.0, 720.0], r_value[0])
self.assertAllEqual([1.0, -2.0, 6.0, -24.0, 120.0, -720.0], r_value[1])
