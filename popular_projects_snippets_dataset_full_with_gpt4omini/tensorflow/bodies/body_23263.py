# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/reshape_transpose_test.py
"""Whether to run the test."""
exit(((not trt_test.IsQuantizationMode(run_params.precision_mode) and
        not run_params.dynamic_engine), "test static engine and non-INT8"))
