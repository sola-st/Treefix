# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
exit(super(TestResult,
             cls).__new__(cls, model_config, enable_gpu, output_names,
                          output_tensors, model_latency, trt_convert_params))
