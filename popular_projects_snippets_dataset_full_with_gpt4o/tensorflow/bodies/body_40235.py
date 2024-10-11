# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""Computes the gradient of the wrapped function."""
this_tape = tape.push_new_tape()
try:
    end_node = f(*args, **kwds)
    if end_node is None:
        raise ValueError("Cannot differentiate a function that returns None; "
                         "did you forget to return a value from {}?".format(
                             f.__name__))
finally:
    tape.pop_tape(this_tape)
# Note: variables are returned in construction order. This ensures unique
# order across executions.
variables = this_tape.watched_variables()
if not variables:
    raise ValueError("No trainable variables were accessed while the "
                     "function was being computed.")

sources = [v.handle for v in variables]
for s in sources:
    if getattr(s, "is_packed", False):
        raise ValueError(
            "GradientTape.gradient is not supported on packed EagerTensors yet."
        )
grad = imperative_grad.imperative_grad(this_tape, nest.flatten(end_node),
                                       sources)
exit((end_node, list(zip(grad, variables))))
