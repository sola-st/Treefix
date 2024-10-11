# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
self._ori_model = self.model_handler_cls(model_config)
self._trt_models = []
for trt_convert_params in trt_convert_params_updater(
    default_trt_convert_params):
    trt_model = self.trt_model_handler_cls(
        model_config, trt_convert_params=trt_convert_params)
    self._trt_models.append(trt_model)

self._name = name
self._result_collection = None
