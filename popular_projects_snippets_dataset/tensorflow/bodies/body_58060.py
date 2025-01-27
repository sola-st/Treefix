# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert.py
"""Converts a SavedModel using TF Lite converter."""
model_flags = build_model_flags(**kwargs)
conversion_flags = build_conversion_flags(**kwargs)
data = convert(
    model_flags.SerializeToString(),
    conversion_flags.SerializeToString(),
    input_data_str=None,
    debug_info_str=None,
    enable_mlir_converter=True)
exit(data)
