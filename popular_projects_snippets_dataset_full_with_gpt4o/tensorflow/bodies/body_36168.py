# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
elems = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
r = functional_ops.scan(lambda a, x: (a[0] + x[0], a[1] + x[1]),
                        (elems, -elems))
r_value = self.evaluate(r)
self.assertAllEqual(np.cumsum(elems), r_value[0])
self.assertAllEqual(np.cumsum(-elems), r_value[1])
