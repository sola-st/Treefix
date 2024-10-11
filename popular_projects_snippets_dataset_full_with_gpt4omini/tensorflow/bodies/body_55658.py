# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
graph1 = ops.Graph()
with graph1.as_default():
    with ops.name_scope("hidden1/hidden2/hidden3"):
        images = constant_op.constant(
            1.0, dtypes.float32, shape=[3, 2], name="images")
        if use_resource:
            weights1 = variables.Variable(
                [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], name="weights")
            biases1 = resource_variable_ops.ResourceVariable(
                [0.1] * 3, name="biases")
        else:
            biases1 = variables.Variable([0.1] * 3, name="biases")
            weights1 = variables.Variable(
                [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], name="weights")
        nn_ops.relu(math_ops.matmul(images, weights1) + biases1, name="relu")

orig_meta_graph, var_list = meta_graph.export_scoped_meta_graph(
    export_scope="hidden1/hidden2", graph=graph1)
var_names = [v.name for _, v in var_list.items()]
self.assertEqual(["hidden3/biases:0", "hidden3/weights:0"],
                 sorted(var_list.keys()))
self.assertEqual([
    "hidden1/hidden2/hidden3/biases:0", "hidden1/hidden2/hidden3/weights:0"
], sorted(var_names))
for node in orig_meta_graph.graph_def.node:
    self.assertTrue(node.name.startswith("hidden3"))

graph2 = ops.Graph()
new_var_list = meta_graph.import_scoped_meta_graph(
    orig_meta_graph, import_scope="new_hidden1/new_hidden2", graph=graph2)
self.assertEqual(["hidden3/biases:0", "hidden3/weights:0"],
                 sorted(new_var_list.keys()))
new_var_names = [v.name for _, v in new_var_list.items()]
self.assertEqual([
    "new_hidden1/new_hidden2/hidden3/biases:0",
    "new_hidden1/new_hidden2/hidden3/weights:0"
], sorted(new_var_names))

nodes = [
    "new_hidden1/new_hidden2/hidden3/biases/Assign",
    "new_hidden1/new_hidden2/hidden3/weights/Assign"
]
expected = [
    b"loc:@new_hidden1/new_hidden2/hidden3/biases",
    b"loc:@new_hidden1/new_hidden2/hidden3/weights"
]
