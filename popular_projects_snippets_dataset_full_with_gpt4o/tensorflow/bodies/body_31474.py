# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
for (data_format, use_gpu) in GetTestConfigs():
    self.ConstructAndTestGradient(
        batch=4,
        input_rows=6,
        input_cols=5,
        filter_rows=2,
        filter_cols=2,
        in_depth=2,
        out_depth=3,
        stride_rows=2,
        stride_cols=2,
        padding="SAME",
        test_input=False,
        data_format=data_format,
        use_gpu=use_gpu)
