# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/quantization_test.py
# Only test FP32/FP16 mode.
exit((not trt_test.IsQuantizationMode(
    run_params.precision_mode), "test non-INT8"))
