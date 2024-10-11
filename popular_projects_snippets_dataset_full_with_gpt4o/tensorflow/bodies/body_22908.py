# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
exit(filter(
    lambda x: x is not None,
    itertools.chain([self.cpu_base_result, self.gpu_base_result],
                    self.trt_results)))
