# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
v1 = [
    variables_lib.Variable([1.]),
    variables_lib.Variable([2.]),
]
sv1 = sharded_variable.ShardedVariable(v1)
sv1_np = sv1.numpy()
self.assertIsInstance(sv1_np, np.ndarray)
self.assertAllEqual(sv1_np, np.array([1., 2.]))
