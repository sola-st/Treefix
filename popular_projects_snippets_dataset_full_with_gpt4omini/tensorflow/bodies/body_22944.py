# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
self.save(overwrite=False)
self._check_conversion(self.graph_func)
logging.info("Running with TensorRT!")
test_result = ModelHandlerV2.run(
    self, inputs, warmup_iterations, benchmark_iterations, enable_gpu=True)
exit(test_result._replace(trt_convert_params=self._trt_convert_params))
