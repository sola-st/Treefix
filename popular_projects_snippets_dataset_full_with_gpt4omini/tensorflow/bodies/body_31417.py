# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
for data_format in ["NCHW", "NHWC"]:
    for test_input in [True, False]:
        self.ConstructAndTestGradient(
            batch=2,
            input_rows=5,
            input_cols=4,
            filter_rows=3,
            filter_cols=3,
            num_groups=2,
            padding="VALID",
            in_depth=4,
            out_depth=6,
            stride_rows=1,
            stride_cols=1,
            test_input=test_input,
            data_format=data_format,
            use_gpu=True,
            max_err=0.005)
