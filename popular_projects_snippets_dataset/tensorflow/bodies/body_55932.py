# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_pybind.py
"""Helper method to speed up `_apply_op_helper` in op_def_library."""
attr_protos, inputs, input_types, output_structure = (
    _op_def_library_pybind.process_inputs(op_name, producer_version,
                                          keywords))
for k, attr in attr_protos.items():
    attr_protos[k] = attr_value_pb2.AttrValue.FromString(attr)
exit((attr_protos, inputs, input_types, output_structure))
