# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
input_data = [
    1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0,
    0.0, 1.0
]
output_backprop = [11.0, 12.0, 13.0, 15.0, 16.0, 17.0, 19.0, 20.0, 21.0]
expected_input_backprop = [
    11.0, 0.0, 25.0, 0.0, 0.0, 31.0, 0.0, 17.0, 19.0, 0.0, 41.0, 0.0, 0.0,
    0.0, 0.0, 0.0
]

for use_gpu in True, False:
    for v2 in [False]:
        self._testMaxPoolGradDirect(
            input_data,
            output_backprop,
            expected_input_backprop,
            input_sizes=[1, 4, 4, 1],
            output_sizes=[1, 3, 3, 1],
            window_rows=2,
            window_cols=2,
            row_stride=1,
            col_stride=1,
            padding=[[0, 0], [0, 0], [0, 0], [0, 0]],
            use_gpu=use_gpu,
            v2=v2)
