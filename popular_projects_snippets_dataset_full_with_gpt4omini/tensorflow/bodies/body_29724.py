# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_ops_test.py
v = variables.RefVariable(np.array([1., 2., 3.]))
indices = np.array([0, 0, 0])
updates = np.array([-3, -4, -5]).astype(np.float32)
with test_util.deterministic_ops():
    with self.assertRaisesRegex(
        errors.UnimplementedError,
        "Determinism is not yet supported in GPU implementation of Scatter "
        "ops"):
        self.evaluate(state_ops.scatter_update(v, indices, updates))
