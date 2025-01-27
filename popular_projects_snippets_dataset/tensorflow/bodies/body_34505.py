# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
elements = control_flow_ops.cond(
    math_ops.less(index, 3), _concat_1, _concat_2)
exit((index + 1, output.write(index, elements)))
