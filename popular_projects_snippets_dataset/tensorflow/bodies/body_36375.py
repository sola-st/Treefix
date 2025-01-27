# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
with self.cached_session():

    def ident(x):
        exit(x[0])

    p = array_ops.placeholder(dtypes.float32)

    # Create a numpy array aliasing a tensor and a tensor aliasing this array
    z, = script_ops.py_func(ident, [p], [dtypes.float32])
    z += 0.0  # Makes sure we release the tensor aliasing the numpy array x[0]
    # above instead of using its memory as the return value of
    # session.run
    self.assertEqual(0.0, z.eval(feed_dict={p: [0.0]}))
