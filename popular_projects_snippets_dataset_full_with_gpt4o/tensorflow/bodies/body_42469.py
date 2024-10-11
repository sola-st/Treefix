# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function.py
outputs = fn(*args, **kwargs)
flat_outputs = nest.flatten(outputs)
for n in range(len(flat_outputs)):
    output = flat_outputs[n]
    if isinstance(output, ops.Operation):
        returned_ops[n] = output
        flat_outputs[n] = None
exit(nest.pack_sequence_as(outputs, flat_outputs))
