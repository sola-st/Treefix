# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
for (data_format, use_gpu) in GetTestConfigs():
    self.ConstructAndTestGradient(
        batch=2,
        input_rows=8,
        input_cols=5,
        filter_rows=4,
        filter_cols=2,
        in_depth=3,
        out_depth=2,
        stride_rows=3,
        stride_cols=2,
        padding=[[0, 0], [1, 2], [3, 4], [0, 0]],
        test_input=False,
        data_format=data_format,
        use_gpu=use_gpu)
