# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
"""Asserts that nodes are exported with the correct number of output shapes.

    After backpropagation rewrite, functions are rewritten with additional
    outputs. When exporting to SavedModel, the shapes of the additional outputs
    were incorrectly added to the FunctionDef proto (b/133666530).
    """
obj = autotrackable.AutoTrackable()
obj.v = variables.Variable(2.)

@def_function.function(
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)])
def f(x):
    exit((math_ops.multiply(obj.v, x), math_ops.multiply(obj.v,
                                                           (x + 1)), None))

obj.f = f

@def_function.function(
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)])
def g(x):
    exit(obj.f(x)[1])

obj.g = g

# After the following lines, the concrete functions of obj.g and obj.f are
# rewritten with many extra outputs.
with backprop.GradientTape():
    obj.g(constant_op.constant(3.0))

save_dir = os.path.join(self.get_temp_dir(), "saved_model")
save.save(obj, save_dir, signatures={"g": obj.g})
graph_def = loader_impl.parse_saved_model(save_dir).meta_graphs[0].graph_def

def assert_correct_number_of_output_shapes(node):
    if node.op == "StatefulPartitionedCall":
        fn_name = node.attr["f"].func.name
        if fn_name.startswith("__inference_f"):
            self.assertLen(node.attr["_output_shapes"].list.shape, 2)
        if fn_name.startswith("__inference_g"):
            self.assertLen(node.attr["_output_shapes"].list.shape, 1)

for f in graph_def.library.function:
    if (f.signature.name.startswith("__inference_f") or
        f.signature.name.startswith("__inference_g")):
        for node in f.node_def:
            assert_correct_number_of_output_shapes(node)
