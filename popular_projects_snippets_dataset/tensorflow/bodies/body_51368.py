# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
"""A 1.x SavedModel with a single variable."""
export_graph = ops.Graph()
with export_graph.as_default():
    v = resource_variable_ops.ResourceVariable(3., **kwargs_for_variable)
    with session_lib.Session() as session:
        session.run([v.initializer])
        path = os.path.join(self.get_temp_dir(), "saved_model", str(ops.uid()))
        b = builder_impl.SavedModelBuilder(path)
        b.add_meta_graph_and_variables(
            session,
            tags=[tag_constants.SERVING],
            signature_def_map={})
        b.save()

exit(path)
