# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
for (data_format, use_gpu) in GetTestConfigs():
    self.ConstructAndTestGradient(
        batch=2,
        input_rows=8,
        input_cols=7,
        filter_rows=4,
        filter_cols=4,
        in_depth=2,
        out_depth=3,
        stride_rows=3,
        stride_cols=3,
        padding="SAME",
        test_input=False,
        data_format=data_format,
        use_gpu=use_gpu)
