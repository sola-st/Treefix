# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
exit(xla.select_and_scatter(
    operand,
    window_dimensions=[2, 3, 1, 1],
    window_strides=[2, 2, 1, 1],
    padding=[[0, 0]] * 4,
    source=source,
    init_value=0,
    select=ge_select,
    scatter=add_scatter))
