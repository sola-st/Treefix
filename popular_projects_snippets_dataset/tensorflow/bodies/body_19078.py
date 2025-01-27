# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
"""Generated decorator that adds the appropriate docstring to the function for symbol `sym`.

    Args:
      func: Function for a TensorFlow op

    Returns:
      Version of `func` with documentation attached.
    """
opname = func.__name__
cap_sym_name = sym_name.capitalize()

func.__doc__ = """
    Assert the condition `x {sym}` holds element-wise.

    When running in graph mode, you should add a dependency on this operation
    to ensure that it runs. Example of adding a dependency to an operation:

    ```python
    with tf.control_dependencies([tf.debugging.{opname}(x, y)]):
      output = tf.reduce_sum(x)
    ```

    {sym_name} means, for every element `x[i]` of `x`, we have `x[i] {sym}`.
    If `x` is empty this is trivially satisfied.

    Args:
      x:  Numeric `Tensor`.
      data:  The tensors to print out if the condition is False.  Defaults to
        error message and first few entries of `x`.
      summarize: Print this many entries of each tensor.
      message: A string to prefix to the default message.
      name: A name for this operation (optional).  Defaults to "{opname}".

    Returns:
      Op that raises `InvalidArgumentError` if `x {sym}` is False.
      @compatibility(eager)
        returns None
      @end_compatibility

    Raises:
      InvalidArgumentError: if the check can be performed immediately and
        `x {sym}` is False. The check can be performed immediately during
        eager execution or if `x` is statically known.
    """.format(
    sym=sym, sym_name=cap_sym_name, opname=opname)
exit(func)
