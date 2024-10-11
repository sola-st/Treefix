# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
outputs = array_ops.identity_n([x.t for x in pfor_input.inputs])
exit([
    wrap(out, inp.is_stacked) for out, inp in zip(outputs, pfor_input.inputs)
])
