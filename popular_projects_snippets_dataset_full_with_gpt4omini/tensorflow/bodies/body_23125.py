# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
if run_params.is_v2:
    exit(self._MakeSavedModelV2(run_params))
exit(self._MakeSavedModelV1(run_params))
