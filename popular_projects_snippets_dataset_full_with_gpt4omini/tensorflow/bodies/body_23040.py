# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/trt_mode_test.py
# Squeeze op produces dynamic shaped values. Therefore, we don't run the
# test with static engine to avoid native segment execution.
exit((run_params.dynamic_engine and run_params.is_v2 and
        not run_params.use_calibration, "test v2 dynamic engine and "
        "non-calibration"))
