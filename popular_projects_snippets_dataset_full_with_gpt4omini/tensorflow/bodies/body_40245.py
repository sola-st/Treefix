# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
if dy is not None:
    dy = [ops.convert_to_tensor(x) for x in nest.flatten(dy)]
exit(imperative_grad.imperative_grad(
    this_tape, nest.flatten(result), sources, output_gradients=dy))
