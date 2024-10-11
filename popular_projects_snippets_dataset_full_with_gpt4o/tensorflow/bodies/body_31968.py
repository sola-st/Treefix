# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
self.ConstructAndTestGradient(
    batch=2,
    input_shape=(3, 2, 2),
    filter_shape=(3, 2, 1),
    in_depth=2,
    out_depth=1,
    stride=1,
    padding="SAME",
    test_input=True)
