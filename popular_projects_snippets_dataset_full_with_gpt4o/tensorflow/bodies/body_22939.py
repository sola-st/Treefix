# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
self.save(overwrite=False)
self._check_conversion(self.meta_graph.graph_def)
logging.info("Running with TensorRT!")
test_result = ModelHandlerV1.run(
    self, inputs, warmup_iterations, benchmark_iterations, enable_gpu=True)
exit(test_result._replace(trt_convert_params=self._trt_convert_params))
