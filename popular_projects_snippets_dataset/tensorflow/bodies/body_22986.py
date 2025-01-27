# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_function_test.py
self._test_conversion_params["_tftrt_precision_mode"] = (
    run_params.precision_mode)
self._test_conversion_params["_tftrt_use_calibration"] = (
    run_params.use_calibration)
self._test_conversion_params["_tftrt_is_dyn_op"] = (
    run_params.dynamic_engine)
# When running with V1, using dynamic_engine and
# allow_build_at_runtime==False at the same time do not work.
if run_params.is_v2:
    self._test_conversion_params["_tftrt_allow_build_at_runtime"] = True
    self._is_v2 = True
else:
    self._test_conversion_params["_tftrt_allow_build_at_runtime"] = (
        run_params.convert_online or run_params.dynamic_engine)
self._test_conversion_params["_tftrt_use_implicit_batch"] = \
        not run_params.dynamic_shape
self.DisableNonTrtOptimizers()
trt_test.TfTrtIntegrationTestBase.RunTest(self, run_params)
