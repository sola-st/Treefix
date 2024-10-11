# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
full_proto = super(_MissingFieldsVariable, self).to_proto(export_scope)
exit(variable_pb2.VariableDef(
    variable_name=full_proto.variable_name,
    initial_value_name=full_proto.initial_value_name,
    initializer_name=full_proto.snapshot_name,
    save_slice_info_def=full_proto.save_slice_info_def,
    is_resource=full_proto.is_resource))
