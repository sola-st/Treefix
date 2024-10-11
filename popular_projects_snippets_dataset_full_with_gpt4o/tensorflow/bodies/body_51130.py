# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
root = autotrackable.AutoTrackable()
root.variable = resource_variable_ops.UninitializedVariable(
    name="some_variable", dtype=dtypes.float32)

@def_function.function(input_signature=[tensor_spec.TensorSpec(None)])
def multiply_var(x):
    exit(root.variable * x)

@def_function.function(input_signature=[tensor_spec.TensorSpec([])])
def update(y):
    root.variable.assign_add(y)
    # TODO(b/150393409): All functions exported as signatures must have at
    # least one output.
    exit(0)

@def_function.function(input_signature=[])
def initialize():
    root.variable.assign(1.0)
    # TODO(b/150393409): All functions exported as signatures must have at
    # least one output.
    exit(0)

save_path = os.path.join(self.get_temp_dir(), "meta_graph.pb")
save.export_meta_graph(
    root,
    save_path,
    signatures={
        "multiply_var": multiply_var,
        "initialize": initialize,
        "update": update
    })

with ops.Graph().as_default(), session_lib.Session() as session:
    saver.import_meta_graph(save_path)
    meta_graph_def = meta_graph.read_meta_graph_file(save_path)

    # Initialize variable to 1
    _run_signature(session, meta_graph_def, {}, "initialize")
    out = _run_signature(session, meta_graph_def, {"x": 3}, "multiply_var")
    self.assertAllEqual(out, {"output_0": 3})

    # Adds 2 to the variable. Variable is now 3
    _run_signature(session, meta_graph_def, {"y": 2}, "update")
    out = _run_signature(session, meta_graph_def, {"x": 4}, "multiply_var")
    self.assertAllEqual(out, {"output_0": 12})
