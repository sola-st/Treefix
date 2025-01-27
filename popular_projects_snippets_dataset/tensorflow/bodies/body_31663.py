# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
input_data = [
    1.0,
    0.0,
    1.0,
    0.0,
    0.0,
    1.0,
    0.0,
    1.0,
    1.0,
    0.0,
    1.0,
    0.0,
    0.0,
    1.0,
    0.0,
    1.0,
]
output_backprop = [
    11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0,
    23.0, 24.0, 25.0, 26.0
]
expected_input_backprop = [
    54,
    0.0,
    62,
    0.0,
    0.0,
    60,
    0.0,
    22.0,
    47,
    0.0,
    51,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
]

for use_gpu in True, False:
    for v2 in [True, False]:
        self._testMaxPoolGradDirect(
            input_data,
            output_backprop,
            expected_input_backprop,
            input_sizes=[1, 4, 4, 1],
            output_sizes=[1, 4, 4, 1],
            window_rows=3,
            window_cols=3,
            row_stride=1,
            col_stride=1,
            padding="SAME",
            use_gpu=use_gpu,
            v2=v2)
