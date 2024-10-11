# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
exit(IsQuantizationMode(
    params.precision_mode) and not params.use_calibration)
