# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode(), test_util.deterministic_ops():
    # Normally a nondeterministic codepath occurs when the variable has at
    # least 1024 elements. Test that op determinism ensures the op is
    # deterministc.
    v = resource_variable_ops.ResourceVariable(array_ops.zeros([1024]))
    delta = ops.IndexedSlices(
        values=np.random.normal(size=(1_000_000,)),
        indices=array_ops.zeros((1_000_000,), dtype=np.int32),
        dense_shape=(1024,))
    v.scatter_add(delta)
    for _ in range(5):
        v2 = resource_variable_ops.ResourceVariable(array_ops.zeros([1024]))
        v2.scatter_add(delta)
        self.assertAllEqual(v, v2)
