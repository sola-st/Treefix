# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
new_inputs = []
for inp in inputs:
    if inp.is_stacked:
        new_inputs.append(wrap(array_ops.gather(inp.t, indices), True))
    else:
        new_inputs.append(inp)
exit(new_inputs)
