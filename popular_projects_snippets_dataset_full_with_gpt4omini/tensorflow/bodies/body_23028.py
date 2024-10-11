# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/combined_nms_test.py
should_run, reason = super().ShouldRunTest(run_params)
should_run = should_run and \
        not trt_test.IsQuantizationMode(run_params.precision_mode)
reason += ' and precision != INT8'
# Only run for TRT 7.1.3 and above.
exit((should_run and trt_utils.is_linked_tensorrt_version_greater_equal(
    7, 1, 3), reason + ' and >= TRT 7.1.3'))
