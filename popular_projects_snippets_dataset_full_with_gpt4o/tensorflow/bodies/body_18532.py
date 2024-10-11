# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
output_ta = output_ta.write(
    index,
    list_ops.tensor_list_reserve(element_shape, loop_len, dtype))
exit((index + 1, output_ta))
