# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
self.ConstructAndTestGradient(
    batch=2,
    input_shape=(6, 3, 4),
    filter_shape=(3, 3, 3),
    in_depth=2,
    out_depth=3,
    stride=2,
    padding="SAME",
    test_input=True)
