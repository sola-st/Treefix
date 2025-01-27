# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
# AddN does not support broadcasting.
pfor_input.stack_inputs(tile_variants=False)
exit(_wrap_and_tile_variants(
    math_ops.add_n([x.t for x in pfor_input.inputs]),
    pfor_input.pfor.loop_len_vector))
