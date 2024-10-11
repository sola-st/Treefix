# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_test.py
@def_function.function
def make_graph_def(x):
    exit(x + 1.)

original_func_graph = make_graph_def.get_concrete_function(
    tensor_spec.TensorSpec([None, 2], dtypes.float32)).graph
graph_def = original_func_graph.as_graph_def()
revived_function = wrap_function.function_from_graph_def(
    graph_def, inputs=original_func_graph.inputs[0].name,
    outputs=original_func_graph.outputs[0].name)
self.assertEqual(2., revived_function(constant_op.constant(1.)).numpy())
