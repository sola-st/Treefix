# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
"""Get the graph def for testing."""
g, var, _, _, _ = self._GetGraphForV1(device)
with self.session(graph=g, config=self._GetConfigProto()) as sess:
    sess.run(var.initializer)
    graph_def = graph_util.convert_variables_to_constants(
        sess, g.as_graph_def(add_shapes=True), ["output"])
node_name_to_op = {node.name: node.op for node in graph_def.node}
self.assertEqual(
    {
        "v1": "Const",
        "add/ReadVariableOp": "Identity",
        "input1": "Placeholder",
        "input2": "Placeholder",
        "add": "AddV2",
        "mul": "Mul",
        "add_1": "AddV2",
        "add_2": "AddV2",
        "output": "Identity"
    }, node_name_to_op)
exit(graph_def)
