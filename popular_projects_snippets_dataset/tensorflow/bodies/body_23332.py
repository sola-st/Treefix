# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Validate the provided TrtConversionParams.

  Args:
    conversion_params: a TrtConversionParams instance.
    is_v2: whether we're getting a RewriterConfig for TF 2.0.

  Raises:
    TypeError: if any of the parameters are of unexpected type.
    ValueError: if any of the parameters are of unexpected value.
  """
supported_precision_modes = TrtPrecisionMode.supported_precision_modes()
if conversion_params.precision_mode not in supported_precision_modes:
    raise ValueError(
        ("precision mode '{}' is not supported."
         "It should be one of {}").format(conversion_params.precision_mode,
                                          supported_precision_modes))
if (conversion_params.minimum_segment_size <= 0 and
    conversion_params.minimum_segment_size != -1):
    raise ValueError("minimum segment size should be positive or -1 "
                     "(to disable main graph conversion).")
