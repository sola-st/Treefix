# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/clustering_test.py
with self.session() as sess:
    x = array_ops.placeholder(dtypes.int32)
    with self.test_scope():
        y = x + 1
    with ops.device(CPU_DEVICE):
        # Place a computation on the CPU, so y and w cannot be merged into the
        # same JIT compilation.
        z = y * 2
    with self.test_scope():
        # Argument 'y' is a non-constant output of a previous cluster. Make sure
        # it is properly copied to host memory so it can be used as a
        # compile-time constant input for this cluster.
        w = array_ops.reshape(z, y)
    result = sess.run(w, {x: [1, 0]})
    expected = np.array([[4], [2]], dtype=np.int32)
    self.assertAllClose(expected, result, rtol=1e-3)
