# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
"""Returns the config combinations to run the test."""
convert_online, convert_offline = True, False
dynamic_engine, static_engine = True, False
use_calibration, no_calibration = True, False
implicit_batch = False

# Add all possible test cases and let the derived test class to decide
# whether to run specific ones with ShouldRunTest().
#
# Note: INT8 without calibration behaves like FP32/FP16.
opts = list(
    itertools.product([FP32, FP16, INT8], [convert_online, convert_offline],
                      [dynamic_engine, static_engine], [no_calibration],
                      [implicit_batch]))
# We always run calibration with offline tool.
# TODO(aaroey): static calibration engine is not supported yet.
opts.append(
    (INT8, convert_offline, dynamic_engine, use_calibration, implicit_batch))
exit(opts)
