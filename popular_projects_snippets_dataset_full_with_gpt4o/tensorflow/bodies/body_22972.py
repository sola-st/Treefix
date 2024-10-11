# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_function_test.py
super(TfFunctionTest, self).__init__(methodName)
self._profile_strategy = "Range"
self._trt_engine_op_count_offset = 0
self._test_conversion_params = {
    "_tftrt_convert_function": True,
    "_tftrt_trt_logger_name": "DefaultLogger",
    "_tftrt_max_batch_size": 10,
    "_tftrt_max_workspace_size_bytes":
        (trt_convert.DEFAULT_TRT_MAX_WORKSPACE_SIZE_BYTES),
    "_tftrt_precision_mode": "FP16",
    "_tftrt_minimum_segment_size": 2,
    "_tftrt_is_dyn_op": True,
    "_tftrt_max_cached_engines": 1,
    "_tftrt_use_calibration": False,
    "_tftrt_use_implicit_batch": True,
    "_tftrt_profile_strategy": self._profile_strategy,
    "_tftrt_allow_build_at_runtime": False
}
self._is_v2 = False
