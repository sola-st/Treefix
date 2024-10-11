# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/int32_test.py
# Although test passes with all configurations but only
# execute INT8 with use_calibration=True because
# that is the purpose of the test.
exit((trt_test.IsQuantizationWithCalibration(
    run_params), 'test calibration and INT8'))
