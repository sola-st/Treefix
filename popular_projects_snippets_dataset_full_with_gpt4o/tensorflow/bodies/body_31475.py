# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
for (data_format, use_gpu) in GetTestConfigs():
    self.ConstructAndTestGradient(
        batch=2,
        input_rows=7,
        input_cols=6,
        filter_rows=3,
        filter_cols=3,
        in_depth=4,
        out_depth=5,
        stride_rows=3,
        stride_cols=3,
        padding="SAME",
        test_input=True,
        data_format=data_format,
        use_gpu=use_gpu)
