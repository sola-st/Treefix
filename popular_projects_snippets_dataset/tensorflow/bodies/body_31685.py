# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
self._ConstructAndTestGradient(
    nn_ops.avg_pool,
    input_sizes=[2, 2, 2, 3],
    output_sizes=[2, 1, 1, 3],
    window_rows=2,
    window_cols=2,
    row_stride=2,
    col_stride=2,
    padding="VALID",
    data_format=data_format,
    use_gpu=use_gpu)
