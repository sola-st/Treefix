# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py
dataset = dataset_ops.Dataset.from_tensors(x)
y = script_ops.py_func(map_py_fn, [x], x.dtype)
dataset = dataset.repeat(y)
exit(dataset)
