# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
exit(super(TrtConversionParams,
             cls).__new__(cls, max_workspace_size_bytes, precision_mode,
                          minimum_segment_size, maximum_cached_engines,
                          use_calibration, allow_build_at_runtime))
