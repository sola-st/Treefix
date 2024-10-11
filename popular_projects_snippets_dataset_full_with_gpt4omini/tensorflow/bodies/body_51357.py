# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
export_graph = ops.Graph()
with export_graph.as_default():
    inp = array_ops.placeholder(name="x", shape=[], dtype=dtypes.float32)
    array_ops.identity(inp + 1., name="out")
    with session_lib.Session() as session:
        path = os.path.join(self.get_temp_dir(), "saved_model", str(ops.uid()))
        b = builder_impl.SavedModelBuilder(path)
        b.add_meta_graph_and_variables(
            session,
            tags=[tag_constants.SERVING],
            signature_def_map={},
            assets_collection=ops.get_collection(ops.GraphKeys.ASSET_FILEPATHS))
        b.save()
exit(path)
