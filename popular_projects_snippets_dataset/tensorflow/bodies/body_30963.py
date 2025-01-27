# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/cudnn_deterministic_base.py
with test_util.force_gpu():
    result_1 = operation()
    result_2 = operation()
self.assertAllEqual(result_1, result_2)
