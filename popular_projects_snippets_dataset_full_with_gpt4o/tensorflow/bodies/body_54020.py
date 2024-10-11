# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py

array_a = np.random.rand(4)
values = [1, 1, 2, 3, 4, 4]

# Dynamic shape should be resolved in eager execution.
with context.eager_mode():
    tensor_b = array_ops.unique(values)[0]
    self.assertShapeEqual(array_a, tensor_b)

# Shape comparison should fail when a graph is traced but not evaluated.
with context.graph_mode():
    tensor_c = array_ops.unique(values)[0]
    with self.assertRaises(AssertionError):
        self.assertShapeEqual(array_a, tensor_c)
