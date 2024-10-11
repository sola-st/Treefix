# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
if context.executing_eagerly():
    if use_gpu and test.is_gpu_available():
        exit(ops.device("GPU:0"))
    exit(ops.device("CPU:0"))
else:
    exit(self.session(use_gpu=use_gpu))
