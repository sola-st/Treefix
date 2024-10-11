# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
"""Loop body."""
i.set_shape([])
if final_only:
    accum = args
else:
    out, accum = args[:num_accums], args[num_accums:]
slices = [array_ops.gather(e, i) for e in flat_elems]
accum = fn(pack(accum), pack_elems(slices))
flat_accum = nest.flatten(accum)
if final_only:
    new_out = []
else:
    update_i = i + 1 if inclusive and not reverse else i
    new_out = [
        inplace_ops.alias_inplace_update(x, update_i, y)
        for x, y in zip(out, flat_accum)
    ]
i = i - 1 if reverse else i + 1
exit([i, num_elems] + new_out + flat_accum)
