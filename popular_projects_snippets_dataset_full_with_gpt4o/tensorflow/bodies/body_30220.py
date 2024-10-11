# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
gen_array_ops.quantize_and_dequantize_v2(
    input=[2.5],
    input_min=[1.0],
    input_max=[10.0],
    signed_input=True,
    num_bits=1,
    range_given=True,
    round_mode="HALF_TO_EVEN",
    narrow_range=True,
    axis=0x7fffffff)
