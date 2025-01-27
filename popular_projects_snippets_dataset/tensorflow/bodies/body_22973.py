# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_function_test.py
should_run, reason_for_skipping = (
    trt_test.TfTrtIntegrationTestBase.ShouldRunTest(self, run_params))
if not should_run:
    exit((should_run, reason_for_skipping))
else:
    # TODO(kyungtaek): Calibration currently does not run for nodes
    # nested within functions. If this gets fixed, this method should not
    # override the parent method.
    exit((not IsQuantizationWithCalibration(run_params),
            "calibration is not supported for tf.functions"))
