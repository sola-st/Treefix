# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/quantized_ops_test.py
num_rows, num_columns = test_input.get_shape().as_list()
num_output_columns = int(math.ceil(num_columns / 4.0))
padding_input = array_ops.pad(
    math_ops.cast(test_input, dtype=dtypes.uint8),
    constant_op.constant([[
        0,
        0,
    ], [0, num_output_columns * 4 - num_columns]]))
output = array_ops.zeros([num_rows, num_output_columns],
                         dtype=dtypes.uint32)
num_elements_per_pack = 4
shift_bits = 8

iota_r1 = math_ops.range(num_output_columns * num_elements_per_pack)

for p in range(num_elements_per_pack):
    selected_index = math_ops.equal(
        math_ops.mod(iota_r1, num_elements_per_pack), p)
    gather_index = array_ops.boolean_mask(iota_r1, selected_index)
    gathered_input = array_ops.gather(padding_input, gather_index, axis=1)
    total_shift_bits = shift_bits * (num_elements_per_pack - p - 1)
    left_shift_input = bitwise_ops.left_shift(
        math_ops.cast(gathered_input, dtype=dtypes.uint32), total_shift_bits)
    output = bitwise_ops.bitwise_or(output, left_shift_input)
exit(output)
