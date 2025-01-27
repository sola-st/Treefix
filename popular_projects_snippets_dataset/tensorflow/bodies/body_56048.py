# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_def_to_graph_test.py
fdef = self._build_function_def()

g = function_def_to_graph.function_def_to_graph(fdef)
self.assertIsNone(g.inputs[0].shape.dims)  # Unknown dims.
self.assertIsNone(g.inputs[1].shape.dims)  # Unknown dims.
self.assertIsNone(g.outputs[0].shape.dims)  # Unknown dims.
self.assertIsNone(g.outputs[1].shape.dims)  # Unknown dims.

g = function_def_to_graph.function_def_to_graph(
    fdef,
    input_shapes=[
        tensor_shape.TensorShape([5]),
        tensor_shape.TensorShape([5])
    ])
self.assertSequenceEqual(g.inputs[0].shape.dims, [5])
self.assertSequenceEqual(g.inputs[1].shape.dims, [5])
self.assertSequenceEqual(g.outputs[0].shape.dims, [5])
self.assertSequenceEqual(g.outputs[1].shape.dims, [5])

g = function_def_to_graph.function_def_to_graph(
    fdef, input_shapes=[None, tensor_shape.TensorShape([5, 7])])
self.assertIsNone(g.inputs[0].shape.dims)
self.assertSequenceEqual(g.inputs[1].shape.dims, [5, 7])
self.assertSequenceEqual(g.outputs[0].shape.dims, [5, 7])
self.assertSequenceEqual(g.outputs[1].shape.dims, [5, 7])

# Should raise a ValueError if the length of input_shapes does not match
# the number of input args in FunctionDef.signature.input_arg.
with self.assertRaises(ValueError):
    g = function_def_to_graph.function_def_to_graph(
        fdef, input_shapes=[tensor_shape.TensorShape([5, 7])])
