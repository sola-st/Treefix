# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/python/xla.py
exit(gen_xla_ops.xla_gather(
    operand,
    start_indices,
    slice_sizes=slice_sizes,
    dimension_numbers=dimension_numbers.SerializeToString(),
    indices_are_sorted=indices_are_sorted,
    name=name))
