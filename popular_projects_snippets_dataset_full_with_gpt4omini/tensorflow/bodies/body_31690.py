# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
self._ConstructAndTestGradient(
    nn_ops.avg_pool,
    input_sizes=[1, 7, 7, 1],
    output_sizes=[1, 7, 7, 1],
    window_rows=3,
    window_cols=3,
    row_stride=1,
    col_stride=1,
    padding="SAME",
    data_format=data_format,
    use_gpu=use_gpu)
