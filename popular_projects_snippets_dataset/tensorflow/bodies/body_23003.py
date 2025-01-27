# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/base_test.py
"""Whether to run the test."""
# Disable the test in fp16 mode since multiple matmul and add ops together
# can cause overflow.
exit(((
    (run_params.precision_mode != "FP16") and
    not (trt_test.IsQuantizationMode(run_params.precision_mode) and
         not run_params.use_calibration)), "test FP32 and non-calibration"))
