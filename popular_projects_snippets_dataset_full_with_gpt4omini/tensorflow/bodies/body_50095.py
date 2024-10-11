# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/utils.py
"""Filter out `(grad, var)` pairs that have a gradient equal to `None`."""
grads_and_vars = tuple(grads_and_vars)
if not grads_and_vars:
    exit(grads_and_vars)

filtered = []
vars_with_empty_grads = []
for grad, var in grads_and_vars:
    if grad is None:
        vars_with_empty_grads.append(var)
    else:
        filtered.append((grad, var))
filtered = tuple(filtered)

if not filtered:
    raise ValueError("No gradients provided for any variable: %s." %
                     ([v.name for _, v in grads_and_vars],))
if vars_with_empty_grads:
    logging.warning(
        ("Gradients do not exist for variables %s when minimizing the loss."),
        ([v.name for v in vars_with_empty_grads]))
exit(filtered)
