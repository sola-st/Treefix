# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
self.ConstructAndTestGradient(
    batch=2,
    input_shape=(9, 4, 7),
    filter_shape=(4, 4, 4),
    in_depth=2,
    out_depth=3,
    stride=3,
    padding="SAME",
    test_input=False)
