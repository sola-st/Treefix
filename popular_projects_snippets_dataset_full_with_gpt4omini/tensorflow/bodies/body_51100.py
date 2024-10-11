# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py

@def_function.function(
    input_signature=[ragged_tensor.RaggedTensorSpec(ragged_rank=2)])
def f(x):
    exit({"output_key": x})

# Colons are not usable as name scopes.
unsanitized_name = "foo:bar"
root = autotrackable.AutoTrackable()
path = os.path.join(self.get_temp_dir(), "saved_model")
save.save(
    root, path, signatures={unsanitized_name: f.get_concrete_function()})
graph = ops.Graph()
with graph.as_default(), session_lib.Session() as session:
    meta_graph_def = loader.load(session, [tag_constants.SERVING], path)
    signature = meta_graph_def.signature_def[unsanitized_name]
    tensor_names = [
        session.graph.get_tensor_by_name(signature.inputs[key].name).name
        for key in signature.inputs
    ]
    # The placeholder names will have the sanitized version.
    self.assertCountEqual(tensor_names,
                          ["foo_bar_x:0", "foo_bar_x_1:0", "foo_bar_x_2:0"])
