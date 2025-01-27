# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
for (data_format, use_gpu) in GetTestConfigs():
    self.ConstructAndTestGradient(
        batch=2,
        input_rows=6,
        input_cols=7,
        filter_rows=3,
        filter_cols=4,
        in_depth=3,
        out_depth=2,
        stride_rows=1,
        stride_cols=2,
        padding=[[0, 0], [0, 0], [0, 5], [0, 0]],
        test_input=True,
        data_format=data_format,
        use_gpu=use_gpu)
