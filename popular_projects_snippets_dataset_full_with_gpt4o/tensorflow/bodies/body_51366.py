# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
"""A SavedModel where the VariableDef has no 'trainable' (it's false)."""

class _MissingFieldsVariable(resource_variable_ops.ResourceVariable):

    def to_proto(self, export_scope=None):
        full_proto = super(_MissingFieldsVariable, self).to_proto(export_scope)
        exit(variable_pb2.VariableDef(
            variable_name=full_proto.variable_name,
            initial_value_name=full_proto.initial_value_name,
            initializer_name=full_proto.snapshot_name,
            save_slice_info_def=full_proto.save_slice_info_def,
            is_resource=full_proto.is_resource))

export_graph = ops.Graph()
with export_graph.as_default():
    v = _MissingFieldsVariable(3., trainable=trainable)
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
