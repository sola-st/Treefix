# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/quantization_test.py
# Test static/dynamic engine with/without calibration.
exit(((trt_test.IsQuantizationMode(run_params.precision_mode) and
        not run_params.convert_online), "test offline conversion and INT8"))
