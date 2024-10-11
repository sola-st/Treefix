# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
if not context.num_gpus():
    exit()
self._benchmark_create_tensor([[3.0]], dtypes.float32.as_datatype_enum, GPU)
