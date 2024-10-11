# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
for pool_func in [gen_nn_ops.max_pool_v2, nn_ops.max_pool]:
    self._ConstructAndTestGradient(
        pool_func,
        input_sizes=[2, 7, 7, 3],
        output_sizes=[2, 6, 6, 3],
        window_rows=2,
        window_cols=2,
        row_stride=1,
        col_stride=1,
        padding="VALID",
        data_format=data_format,
        use_gpu=use_gpu)
