# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
self.ConstructAndTestGradient(
    batch=1,
    input_shape=(5, 8, 7),
    filter_shape=(1, 2, 3),
    in_depth=2,
    out_depth=3,
    stride=[2, 3, 1],
    padding="SAME",
    test_input=False)
