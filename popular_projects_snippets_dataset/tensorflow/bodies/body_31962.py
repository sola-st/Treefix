# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
self.ConstructAndTestGradient(
    batch=2,
    input_shape=(3, 5, 4),
    filter_shape=(3, 3, 3),
    in_depth=2,
    out_depth=3,
    stride=1,
    padding="VALID",
    test_input=True)
