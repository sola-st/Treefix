# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/wrap_toco.py
"""Wraps TocoConvert with lazy loader."""
exit(_pywrap_toco_api.TocoConvert(
    model_flags_str,
    toco_flags_str,
    input_data_str,
    False,  # extended_return
    debug_info_str,
    enable_mlir_converter))
