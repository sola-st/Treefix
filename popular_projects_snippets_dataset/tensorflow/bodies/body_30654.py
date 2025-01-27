# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batch_scatter_ops_test.py
params = np.array([1, 2, 3, 4, 5, 6]).astype(np.float32)
updates = np.array([-3, -4, -5]).astype(np.float32)

ref = variables.Variable(params)
self.evaluate(variables.variables_initializer([ref]))

# Indices all in range, no problem.
indices = np.array([2, 0, 5])
self.evaluate(state_ops.batch_scatter_update(ref, indices, updates))

# Test some out of range errors.
indices = np.array([-1, 0, 5])
with self.assertRaisesOpError(
    r'indices\[0\] = \[-1\] does not index into shape \[6\]'):
    self.evaluate(state_ops.batch_scatter_update(ref, indices, updates))

indices = np.array([2, 0, 6])
with self.assertRaisesOpError(r'indices\[2\] = \[6\] does not index into '
                              r'shape \[6\]'):
    self.evaluate(state_ops.batch_scatter_update(ref, indices, updates))
