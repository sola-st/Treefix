# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
exit(super(TestResultCollection,
             cls).__new__(cls, test_name, model_config, cpu_base_result,
                          gpu_base_result, trt_results))
