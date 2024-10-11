# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/lru_cache_test.py
exit(((run_params.dynamic_engine and not trt_test.IsQuantizationMode(
    run_params.precision_mode)), "test dynamic engine and non-INT8"))
