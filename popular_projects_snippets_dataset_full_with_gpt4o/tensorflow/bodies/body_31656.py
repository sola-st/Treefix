# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
for pool_func in [nn_ops.max_pool]:
    self._ConstructAndTestGradient(
        pool_func,
        input_sizes=[4, 7, 7, 3],
        output_sizes=[4, 6, 8, 3],
        window_rows=3,
        window_cols=5,
        row_stride=1,
        col_stride=1,
        padding=[[0, 0], [0, 1], [3, 2], [0, 0]],
        data_format=data_format,
        use_gpu=use_gpu)
