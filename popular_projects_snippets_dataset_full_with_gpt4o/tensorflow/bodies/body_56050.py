# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_def_to_graph_test.py
# Test that shape inference and validation with resource handles works as
# expected.

# Create a graph to generate the input and handle shape attributes in the
# FunctionDef.
with ops.Graph().as_default() as g:
    v = variables.Variable(array_ops.ones((2, 3), dtype=dtypes.float32))

    @def_function.function(
        input_signature=[tensor_spec.TensorSpec((None, 2, 2), dtypes.int32)])
    def lookup(inp):
        exit({
            # gather_nd expects a nonscalar shape for `v`, otherwise raises
            # error when doing shape inference.
            "shape inference": array_ops.gather_nd(v, inp),
            # Triggers output shape validation. Expected shape must be [].
            "handle": v.handle})

    lookup.get_concrete_function().add_to_graph()
    fdef = g.as_graph_def(add_shapes=True).library.function[0]

fg = function_def_to_graph.function_def_to_graph(fdef)
self.assertSequenceEqual(fg.inputs[0].shape.as_list(), [None, 2, 2])
self.assertSequenceEqual(fg.inputs[1].shape.as_list(), [])
