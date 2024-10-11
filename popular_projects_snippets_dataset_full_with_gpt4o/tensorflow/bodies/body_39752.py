# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
# int32's are kept on host memory even when executing on GPU.
if not context.num_gpus():
    exit()
self._benchmark_create_tensor([[3]], dtypes.int32.as_datatype_enum, GPU)
