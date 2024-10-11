# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_test.py
a_constant_name = "a_constant"
b_constant_name = "b_constant"
c_constant_name = "c_constant"
a_check_name = "a_check"
b_check_name = "b_check"
a_identity_name = "a_identity"
b_identity_name = "b_identity"
c_identity_name = "c_identity"
add_name = "add"
sub_name = "sub"
graph_def = graph_pb2.GraphDef()
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
c_constant = self.create_constant_node_def(
    c_constant_name, value=1, dtype=dtypes.float32, shape=[]
)
graph_def.node.extend([c_constant])
c_identity_node = self.create_node_def(
    "Identity", c_identity_name, [c_constant_name]
)
graph_def.node.extend([c_identity_node])

sub_node = self.create_node_def(
    "Sub", sub_name, [c_constant_name, c_identity_name]
)
self.set_attr_list(sub_node, "_class", [compat.as_bytes(c_identity_name)])
graph_def.node.extend([sub_node])

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
c_constant = self.create_constant_node_def(
    c_constant_name, value=1, dtype=dtypes.float32, shape=[]
)
expected_output.node.extend([c_constant])
c_identity_node = self.create_node_def(
    "Identity", c_identity_name, [c_constant_name]
)
expected_output.node.extend([c_identity_node])

sub_node = self.create_node_def(
    "Sub", sub_name, [c_constant_name, c_identity_name]
)
self.set_attr_list(sub_node, "_class", [compat.as_bytes(c_identity_name)])
expected_output.node.extend([sub_node])

output = graph_util.remove_training_nodes(graph_def)
self.assertProtoEquals(expected_output, output)
