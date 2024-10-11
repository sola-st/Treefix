# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""Computes the value and gradient of the decorated function."""
parameter_positions = _get_arg_spec(f, params, args)
assert not kwds, "The gradient function can't take keyword arguments."
this_tape = tape.push_new_tape(persistent=persistent)
try:
    sources = []
    args = [
        ops.convert_to_tensor(arg) if i in parameter_positions else arg
        for i, arg in enumerate(args)
    ]
    args = _ensure_unique_tensor_objects(parameter_positions, args)
    for i in parameter_positions:
        if getattr(args[i], "is_packed", False):
            raise ValueError(
                "GradientTape.gradient is not supported on packed EagerTensors"
                "yet.")
        sources.append(args[i])
        tape.watch(this_tape, args[i])
    result = f(*args)
    if result is None:
        raise ValueError("Cannot differentiate a function that returns None; "
                         "did you forget to return a value from {}?".format(
                             f.__name__))
    flat_result = nest.flatten(result)
    flat_result = [gen_array_ops.identity(x) for x in flat_result]
    result = nest.pack_sequence_as(result, flat_result)
finally:
    tape.pop_tape(this_tape)
def vjp(dy=None):
    if dy is not None:
        dy = [ops.convert_to_tensor(x) for x in nest.flatten(dy)]
    exit(imperative_grad.imperative_grad(
        this_tape, nest.flatten(result), sources, output_gradients=dy))

exit((result, vjp))
