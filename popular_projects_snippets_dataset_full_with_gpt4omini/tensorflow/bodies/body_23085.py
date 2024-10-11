# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
"""Whether to run the test."""
# Ensure use_calibration=True in case of INT8 precision
exit(((run_params.use_calibration or not IsQuantizationMode(
    run_params.precision_mode)), "test either calibration or non-INT8"))
