# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
output_graph_def = self._ConvertGraphV1(
    minimum_segment_size=minimum_segment_size)
node_name_to_op = {node.name: node.op for node in output_graph_def.node}
self.assertEqual(
    {
        "v1": "Const",
        "input1": "Placeholder",
        "input2": "Placeholder",
        "add": "AddV2",
        "mul": "Mul",
        "add_1": "AddV2",
        "add_2": "AddV2",
        "output": "Identity"
    }, node_name_to_op)
