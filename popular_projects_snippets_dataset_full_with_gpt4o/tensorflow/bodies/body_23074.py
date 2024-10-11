# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
super(TfTrtIntegrationTestBase, self).__init__(methodName)
self._trt_test_params = None
self._disable_non_trt_optimizers = False
self._profile_strategy = "ImplicitBatchModeCompatible"
