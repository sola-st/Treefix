# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/wrap_toco.py
"""Wraps experimental mlir quantize model."""
exit(_pywrap_toco_api.ExperimentalMlirQuantizeModel(
    input_data_str, disable_per_channel, fully_quantize, inference_type,
    input_data_type, output_data_type, enable_numeric_verify,
    enable_whole_model_verify, denylisted_ops, denylisted_nodes,
    enable_variable_quantization))
