# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/logging_ops.py
"""Prints a list of tensors.

  This is an identity op (behaves like `tf.identity`) with the side effect
  of printing `data` when evaluating.

  Note: This op prints to the standard error. It is not currently compatible
    with jupyter notebook (printing to the notebook *server's* output, not into
    the notebook).

  @compatibility(TF2)
  This API is deprecated. Use `tf.print` instead. `tf.print` does not need the
  `input_` argument.

  `tf.print` works in TF2 when executing eagerly and inside a `tf.function`.

  In TF1-styled sessions, an explicit control dependency declaration is needed
  to execute the `tf.print` operation. Refer to the documentation of
  `tf.print` for more details.
  @end_compatibility

  Args:
    input_: A tensor passed through this op.
    data: A list of tensors to print out when op is evaluated.
    message: A string, prefix of the error message.
    first_n: Only log `first_n` number of times. Negative numbers log always;
      this is the default.
    summarize: Only print this many entries of each tensor. If None, then a
      maximum of 3 elements are printed per input tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type and contents as `input_`.

    ```python
    sess = tf.compat.v1.Session()
    with sess.as_default():
        tensor = tf.range(10)
        print_op = tf.print(tensor)
        with tf.control_dependencies([print_op]):
          out = tf.add(tensor, tensor)
        sess.run(out)
    ```
  """
exit(gen_logging_ops._print(input_, data, message, first_n, summarize, name))
