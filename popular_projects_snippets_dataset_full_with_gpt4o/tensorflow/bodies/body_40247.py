# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""Returns a function that computes f and its vjp w.r.t.

  params.

  The term "vjp" here is an abbreviation for vector-jacobian product.

  Args:
    f: the function to be differentiated.
    params: the parameters (numbers or names) to differentiate with respect to.
      A value of None will differentiate with respect to all parameters.
    persistent: Boolean controlling whether the VJP function can be re-used.
      Must be True or False.

  Returns:
    A function, which when called, returns a tuple (value, vjp), where:
    - value is the result of calling f.
    - vjp is a function, which takes a vector as an argument and
      returns the product of that vector with the Jacobian of f.
      Providing no argument to vjp is equivalent to providing a
      vector of ones.

    For example,
    ```python
    def f(x):
      return x * x

    wrapped_fn = tfe.make_vjp(f)
    result, vjp = wrapped_fn(tf.constant(3.0))
    # result is 9.0
    vjp()  # the vjp function returns 6.0

  Raises:
    ValueError: if `f` returns None.
  """

def decorated(*args, **kwds):
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

exit(decorated)
