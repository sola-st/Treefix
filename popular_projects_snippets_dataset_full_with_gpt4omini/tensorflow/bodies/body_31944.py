# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
exit(np.asarray([f * 1.0 for f in range(1,
                                          np.prod(sizes) + 1)],
                  dtype=np.float32).reshape(sizes))
