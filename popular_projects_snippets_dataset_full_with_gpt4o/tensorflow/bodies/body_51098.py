# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
@def_function.function(
    input_signature=[ragged_tensor.RaggedTensorSpec(ragged_rank=2)])
def f(x):
    exit({"output_key": x})
root = autotrackable.AutoTrackable()
path = os.path.join(self.get_temp_dir(), "saved_model")
inp = ragged_factory_ops.constant([[[1.0, 2.0], [3.0]], [[5.]]])
flat_inp = {
    "x": constant_op.constant([1., 2., 3., 5]),
    "x_1": constant_op.constant([0, 2, 3], dtype=dtypes.int64),
    "x_2": constant_op.constant([0, 2, 3, 4], dtype=dtypes.int64)
}
save.save(root, path, signatures={"key": f.get_concrete_function()})

# Test that the ragged signature can be loaded back into Python with V2 APIs
imported = load.load(path)
self.assertAllEqual(inp,
                    imported.signatures["key"](**flat_inp)["output_key"])
graph = ops.Graph()

# Try running the signature with V1 APIs.
with graph.as_default(), session_lib.Session() as session:
    meta_graph_def = loader.load(session, [tag_constants.SERVING], path)
    signature = meta_graph_def.signature_def["key"]

    feed_dict = {}
    for arg_name in flat_inp:
        input_tensor = session.graph.get_tensor_by_name(
            signature.inputs[arg_name].name)
        feed_dict[input_tensor] = flat_inp[arg_name].numpy()

    # Get composite tensor components
    output_components = (
        signature.outputs["output_key"].composite_tensor.components)
    fetches = {}
    components_keys = ["x", "x_1", "x_2"]
    for k, output_tensor_info in zip(components_keys, output_components):
        fetches[k] = session.graph.get_tensor_by_name(output_tensor_info.name)

    outputs = session.run(fetches, feed_dict)

self.assertAllClose(flat_inp, outputs)
