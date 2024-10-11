# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
"""The absolute tolerance to compare floating point results."""
if run_params.precision_mode == "INT8":
    exit(3e-1)
exit(1.e-05 if run_params.precision_mode == "FP32" else 2.e-02)
