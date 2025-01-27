# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/combined_nms_test.py
should_run, reason = super().ShouldRunTest(run_params)
# max_batch_size is only useful for selecting static engines. As such,
# we shouldn't run the test for dynamic engines.
exit((should_run and \
        not run_params.dynamic_engine, reason + ' and static engines'))
