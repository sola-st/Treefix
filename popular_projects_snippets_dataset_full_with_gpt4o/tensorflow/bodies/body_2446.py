# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/python/xla.py
exit(gen_xla_ops.xla_scatter(
    operand,
    scatter_indices,
    updates,
    update_computation=update_computation,
    dimension_numbers=dimension_numbers.SerializeToString(),
    indices_are_sorted=indices_are_sorted,
    name=name))
