# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
graph1 = ops.Graph()
with graph1.as_default():
    with ops.name_scope("hidden1/hidden2/hidden3"):
        images = constant_op.constant(
            1.0, dtypes.float32, shape=[3, 2], name="images")
        weights1 = variables.Variable([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]],
                                      name="weights")
        biases1 = resource_variable_ops.ResourceVariable(
            [0.1] * 3, name="biases")
        nn_ops.relu(math_ops.matmul(images, weights1) + biases1, name="relu")
func_named_operations = []
for op in graph1.get_operations():
    func_named_operations.append(("", op))
debug_info_def = error_interpolation.create_graph_debug_info_def(
    func_named_operations)

# The unique file names in all the stack traces should be larger or equal
# than 1.
self.assertTrue(len(debug_info_def.files) >= 1)
# All the nodes from the exported graphdef are included.
self.assertEqual(len(debug_info_def.traces), len(graph1.get_operations()))
