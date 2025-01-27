# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/lrn_op_test.py
for _ in range(2):
    self._RunAndVerify(dtypes.float32)
    # Enable when LRN supports tf.float16 on GPU.
    if not test.is_gpu_available():
        self._RunAndVerify(dtypes.float16)
