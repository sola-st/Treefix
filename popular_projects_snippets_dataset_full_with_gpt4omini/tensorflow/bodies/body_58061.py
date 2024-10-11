# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert.py
"""Converts a Jax hlo-based model using TFLite converter."""
model_flags = _model_flags_pb2.ModelFlags()
model_flags.use_hlo_import = True
if is_proto_format:
    model_flags.hlo_file_type = _model_flags_pb2.ModelFlags.HLO_PROTO
else:
    model_flags.hlo_file_type = _model_flags_pb2.ModelFlags.HLO_TEXT

# Build input names.
for input_name in input_names:
    input_array = model_flags.input_arrays.add()
    input_array.name = input_name

conversion_flags = build_conversion_flags(**kwargs)
data = convert(
    model_flags.SerializeToString(),
    conversion_flags.SerializeToString(),
    input_data_str=input_content,
    debug_info_str=None,
    enable_mlir_converter=True)
exit(data)
