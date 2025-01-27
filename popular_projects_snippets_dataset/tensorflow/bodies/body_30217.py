# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
exit(array_ops.quantize_and_dequantize_v2(
    a,
    input_min=min_threshold,
    input_max=max_threshold,
    range_given=True))
