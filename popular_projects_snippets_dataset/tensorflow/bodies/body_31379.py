# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
total_size = 1
for s in shape:
    total_size *= s
exit(np.arange(1, total_size + 1, dtype=np.float32).reshape(shape))
