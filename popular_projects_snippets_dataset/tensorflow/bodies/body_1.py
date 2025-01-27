# Extracted from ./data/repos/tensorflow/tensorflow/tools/graph_transforms/python/transform_graph_test.py
input_graph_def = graph_pb2.GraphDef()

const_op1 = input_graph_def.node.add()
const_op1.op = "Const"
const_op1.name = "const_op1"
const_op1.attr["dtype"].CopyFrom(attr_value_pb2.AttrValue(
    type=dtypes.float32.as_datatype_enum))
const_op1.attr["value"].CopyFrom(
    attr_value_pb2.AttrValue(tensor=tensor_util.make_tensor_proto(
        [1, 2], dtypes.float32, [1, 2])))

const_op2 = input_graph_def.node.add()
const_op2.op = "Const"
const_op2.name = "const_op2"
const_op2.attr["dtype"].CopyFrom(attr_value_pb2.AttrValue(
    type=dtypes.float32.as_datatype_enum))
const_op2.attr["value"].CopyFrom(
    attr_value_pb2.AttrValue(tensor=tensor_util.make_tensor_proto(
        [3, 4], dtypes.float32, [1, 2])))

# Create an add that has two constants as inputs.
add_op = input_graph_def.node.add()
add_op.op = "Add"
add_op.attr["T"].CopyFrom(attr_value_pb2.AttrValue(
    type=dtypes.float32.as_datatype_enum))
add_op.name = "add_op"
add_op.input.extend(["const_op1", "const_op2"])

# Create a relu that reads from the add.
relu_op = input_graph_def.node.add()
relu_op.op = "Relu"
relu_op.attr["T"].CopyFrom(attr_value_pb2.AttrValue(
    type=dtypes.float32.as_datatype_enum))
relu_op.name = "relu_op"
relu_op.input.extend(["add_op"])

# We're specifying that add_op is the final output, and so the relu isn't
# needed.
input_names = []
output_names = ["add_op"]
transforms = ["strip_unused_nodes"]
transformed_graph_def = TransformGraph(input_graph_def, input_names,
                                       output_names, transforms)

# We expect that the relu is no longer present after running the transform.
for node in transformed_graph_def.node:
    self.assertNotEqual("Relu", node.op)
