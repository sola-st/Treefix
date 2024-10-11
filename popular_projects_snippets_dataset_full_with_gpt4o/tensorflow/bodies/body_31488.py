# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
for (data_format, use_gpu) in GetTestConfigs():
    self.ConstructAndTestGradient(
        batch=3,
        input_rows=5,
        input_cols=7,
        filter_rows=3,
        filter_cols=2,
        in_depth=1,
        out_depth=2,
        stride_rows=2,
        stride_cols=1,
        padding=[[0, 0], [4, 3], [2, 1], [0, 0]],
        test_input=True,
        data_format=data_format,
        use_gpu=use_gpu)
