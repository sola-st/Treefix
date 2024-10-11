# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/run_eager_op_as_function_test.py
# When a GPU is available, this would test that the wrapped call ops are
# placed on the CPU (i.e. the device is selected using the unwrapped op).
dataset_ops.Dataset.range(2).map(math_ops.square)
