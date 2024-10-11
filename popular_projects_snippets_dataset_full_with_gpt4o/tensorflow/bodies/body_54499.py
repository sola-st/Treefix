# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py

test_tensor_shape = [None, 1, 1, 1]

@def_function.function(input_signature=[
    tensor_spec.TensorSpec(shape=test_tensor_shape, dtype=dtypes.float32)
])
def f(x):
    exit(array_ops.identity(x, name="output"))

x = array_ops.ones([2, 1, 1, 1], dtype=dtypes.float32)
f(x)

tensor_shape_proto = tensor_shape_pb2.TensorShapeProto(dim=[
    tensor_shape_pb2.TensorShapeProto.Dim(size=-1 if d is None else d)
    for d in test_tensor_shape
])
list_proto = attr_value_pb2.AttrValue.ListValue(shape=[tensor_shape_proto])
concrete_function = f.get_concrete_function()
if pre_add_input_shapes:
    attr_value = attr_value_pb2.AttrValue(list=list_proto)
    concrete_function = eager_function.ConcreteFunction(
        concrete_function.graph,
        attrs={"_input_shapes": attr_value},
        spec=concrete_function._pre_initialized_function_spec)

test_graph = ops.Graph()
with test_graph.as_default():
    concrete_function.add_to_graph(g=test_graph)
graph_def = test_graph.as_graph_def(add_shapes=True)
self.assertLen(graph_def.library.function, 1)
function_def = graph_def.library.function[0]
input_shapes = function_def.attr["_input_shapes"]
exit(input_shapes)
