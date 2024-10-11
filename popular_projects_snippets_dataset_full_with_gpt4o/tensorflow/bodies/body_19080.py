# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
"""Generated decorator that adds the appropriate docstring to the function for symbol `sym`.

    Args:
      func: Function for a TensorFlow op

    Returns:
      A version of `func` with documentation attached.
    """
opname = func.__name__

func.__doc__ = """
    Assert the condition `x {sym} y` holds element-wise.

    This condition holds if for every pair of (possibly broadcast) elements
    `x[i]`, `y[i]`, we have `x[i] {sym} y[i]`.
    If both `x` and `y` are empty, this is trivially satisfied.

    When running in graph mode, you should add a dependency on this operation
    to ensure that it runs. Example of adding a dependency to an operation:

    ```python
    with tf.control_dependencies([tf.compat.v1.{opname}(x, y)]):
      output = tf.reduce_sum(x)
    ```

    Args:
      x:  Numeric `Tensor`.
      y:  Numeric `Tensor`, same dtype as and broadcastable to `x`.
      data:  The tensors to print out if the condition is False.  Defaults to
        error message and first few entries of `x`, `y`.
      summarize: Print this many entries of each tensor.
      message: A string to prefix to the default message.
      name: A name for this operation (optional).  Defaults to "{opname}".

    Returns:
      Op that raises `InvalidArgumentError` if `x {sym} y` is False.

    Raises:
      InvalidArgumentError: if the check can be performed immediately and
        `x {sym} y` is False. The check can be performed immediately during
        eager execution or if `x` and `y` are statically known.

    @compatibility(TF2)
    `tf.compat.v1.{opname}` is compatible with eager execution and
    `tf.function`.
    Please use `tf.debugging.{opname}` instead when migrating to TF2. Apart
    from `data`, all arguments are supported with the same argument name.

    If you want to ensure the assert statements run before the
    potentially-invalid computation, please use `tf.control_dependencies`,
    as tf.function auto-control dependencies are insufficient for assert
    statements.

    #### Structural Mapping to Native TF2

    Before:

    ```python
    tf.compat.v1.{opname}(
      x=x, y=y, data=data, summarize=summarize,
      message=message, name=name)
    ```

    After:

    ```python
    tf.debugging.{opname}(
      x=x, y=y, message=message,
      summarize=summarize, name=name)
    ```

    #### TF1 & TF2 Usage Example

    TF1:

    >>> g = tf.Graph()
    >>> with g.as_default():
    ...   a = tf.compat.v1.placeholder(tf.float32, [2])
    ...   b = tf.compat.v1.placeholder(tf.float32, [2])
    ...   result = tf.compat.v1.{opname}(a, b,
    ...     message='"a {sym} b" does not hold for the given inputs')
    ...   with tf.compat.v1.control_dependencies([result]):
    ...     sum_node = a + b
    >>> sess = tf.compat.v1.Session(graph=g)
    >>> val = sess.run(sum_node, feed_dict={{a: [1, 2], b:{test_var}}})


    TF2:

    >>> a = tf.Variable([1, 2], dtype=tf.float32)
    >>> b = tf.Variable({test_var}, dtype=tf.float32)
    >>> assert_op = tf.debugging.{opname}(a, b, message=
    ...   '"a {sym} b" does not hold for the given inputs')
    >>> # When working with tf.control_dependencies
    >>> with tf.control_dependencies([assert_op]):
    ...   val = a + b

    @end_compatibility
    """.format(
    sym=sym, opname=opname, test_var=test_var)
exit(func)
