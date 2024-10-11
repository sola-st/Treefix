# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
with self.cached_session() as sess:
    s = array_ops.placeholder(dtypes.float32, shape=[None])
    b = array_ops.placeholder(dtypes.bool)

    with ops.control_dependencies([b]):
        c = functional_ops.scan(lambda a, x: x * a, s)
    self.assertAllClose(
        np.array([1.0, 3.0, 9.0]), sess.run(c, {s: [1, 3, 3],
                                                b: True}))
