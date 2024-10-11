# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
self.ConstructAndTestGradient(
    batch=2,
    input_shape=(7, 6, 5),
    filter_shape=(2, 2, 2),
    in_depth=2,
    out_depth=3,
    stride=2,
    padding="VALID",
    test_input=False)
