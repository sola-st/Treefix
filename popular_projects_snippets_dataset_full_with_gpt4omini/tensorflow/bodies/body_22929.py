# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
super(_TrtModelHandlerBase, self).__init__(model_config)
self._trt_convert_params = trt_convert_params

self._converter = self._create_converter(trt_convert_params)
self._conversion_is_saved = False
