# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
pfor_input.stack_inputs()
exit(wrap(
    gen_optional_ops.optional_from_value([x.t for x in pfor_input.inputs]),
    True,
))
