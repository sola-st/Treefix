# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
for (data_format, use_gpu) in GetTestConfigs():
    self.ConstructAndTestGradient(
        batch=2,
        input_rows=4,
        input_cols=5,
        filter_rows=3,
        filter_cols=3,
        in_depth=2,
        out_depth=3,
        stride_rows=2,
        stride_cols=2,
        padding=[[0, 0], [1, 1], [1, 1], [0, 0]],
        test_input=True,
        data_format=data_format,
        use_gpu=use_gpu)
