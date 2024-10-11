# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
"""Returns the config combinations to run the test."""
convert_offline = False
# TODO(laigd): add support for static_engine.
dynamic_engine = True
# TODO(laigd): add support for calibration.
no_calibration = False
use_calibration = True

# Add all possible test cases and let the derived test class to decide
# whether to run specific ones with ShouldRunTest().
#
# Note:
# - In TF2.0 the conversion always produce dynamic engine, and we don't test
#   the offline mode here.
# - For simplicity we don't test online conversion which requires setting the
#   Grappler config in default eager context.
# - INT8 without calibration behaves like FP32/FP16.
opts = list(
    itertools.product([FP32, FP16], [convert_offline], [dynamic_engine],
                      [no_calibration], [False, True]))
# We always run calibration with offline tool.
opts.append((INT8, convert_offline, dynamic_engine, use_calibration, False))
opts.append((INT8, convert_offline, dynamic_engine, use_calibration, True))
exit(opts)
