# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/conv2d_test.py
"""The absolute tolerance to compare floating point results."""
if trt_test.IsQuantizationWithCalibration(run_params):
    exit(4e-02)
exit(super(Conv2DNCHWTest, self).ExpectedAbsoluteTolerance(run_params))
