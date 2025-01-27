# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Ensure the `quantized_input_stats` flag is provided if required."""

quantized_types = frozenset({_dtypes.int8, _dtypes.uint8})

requires_quantized_input_stats = (
    (converter_kwargs["inference_type"] in quantized_types or
     converter_kwargs["inference_input_type"] in quantized_types) and
    not quant_mode.is_post_training_integer_quantization())

if (requires_quantized_input_stats and
    not converter_kwargs["quantized_input_stats"]):
    raise ValueError(
        "The `quantized_input_stats` flag must be defined when either "
        "`inference_type` flag or `inference_input_type` flag is set to "
        "tf.int8 or tf.uint8. Currently, `inference_type={}` and "
        "`inference_input_type={}`.".format(
            _get_tf_type_name(converter_kwargs["inference_type"]),
            _get_tf_type_name(converter_kwargs["inference_input_type"])))
