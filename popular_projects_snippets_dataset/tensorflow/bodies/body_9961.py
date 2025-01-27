# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/optimize_for_inference_test.py
self.maxDiff = 1000
unused_constant_name = "unused_constant"
unconnected_add_name = "unconnected_add"
a_constant_name = "a_constant"
b_constant_name = "b_constant"
a_check_name = "a_check"
b_check_name = "b_check"
a_identity_name = "a_identity"
b_identity_name = "b_identity"
add_name = "add"
unused_output_add_name = "unused_output_add"
graph_def = graph_pb2.GraphDef()
unused_constant = self.create_constant_node_def(
    unused_constant_name, value=0, dtype=dtypes.float32, shape=[])
graph_def.node.extend([unused_constant])
unconnected_add_node = self.create_node_def(
    "Add", unconnected_add_name,
    [unused_constant_name, unused_constant_name])
self.set_attr_dtype(unconnected_add_node, "T", dtypes.float32)
graph_def.node.extend([unconnected_add_node])
a_constant = self.create_constant_node_def(
    a_constant_name, value=1, dtype=dtypes.float32, shape=[])
graph_def.node.extend([a_constant])
a_check_node = self.create_node_def("CheckNumerics", a_check_name,
                                    [a_constant_name])
graph_def.node.extend([a_check_node])
a_identity_node = self.create_node_def(
    "Identity", a_identity_name, [a_constant_name, "^" + a_check_name])
graph_def.node.extend([a_identity_node])
b_constant = self.create_constant_node_def(
    b_constant_name, value=1, dtype=dtypes.float32, shape=[])
graph_def.node.extend([b_constant])
b_check_node = self.create_node_def("CheckNumerics", b_check_name,
                                    [b_constant_name])
graph_def.node.extend([b_check_node])
b_identity_node = self.create_node_def(
    "Identity", b_identity_name, [b_constant_name, "^" + b_check_name])
graph_def.node.extend([b_identity_node])
add_node = self.create_node_def("Add", add_name,
                                [a_identity_name, b_identity_name])
self.set_attr_dtype(add_node, "T", dtypes.float32)
graph_def.node.extend([add_node])
unused_output_add_node = self.create_node_def("Add", unused_output_add_name,
                                              [add_name, b_constant_name])
self.set_attr_dtype(unused_output_add_node, "T", dtypes.float32)
graph_def.node.extend([unused_output_add_node])

expected_output = graph_pb2.GraphDef()
a_constant = self.create_constant_node_def(
    a_constant_name, value=1, dtype=dtypes.float32, shape=[])
expected_output.node.extend([a_constant])
b_constant = self.create_constant_node_def(
    b_constant_name, value=1, dtype=dtypes.float32, shape=[])
expected_output.node.extend([b_constant])
add_node = self.create_node_def("Add", add_name,
                                [a_constant_name, b_constant_name])
self.set_attr_dtype(add_node, "T", dtypes.float32)
expected_output.node.extend([add_node])

output = optimize_for_inference_lib.optimize_for_inference(
    graph_def, [], [add_name], dtypes.float32.as_datatype_enum)
self.assertProtoEquals(expected_output, output)
