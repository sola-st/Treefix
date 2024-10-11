# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_gradients.py
"""Create a debug identity tensor that registers and forwards gradients.

    The side effect of this method is that when gradient tensor(s) are created
    with respect to the any paths that include the `input_tensor`, the gradient
    tensor(s) with respect to `input_tensor` will be registered with this
    this `GradientsDebugger` instance and can later be retrieved, with the
    methods `gradient_tensor` and `gradient_tensors`.

    Example:

    ```python
    x = tf.Variable(1.0)
    y = tf.add(x, x)

    grad_debugger = tf_debug.GradientsDebugger()
    debug_y = grad_debugger.identify_gradient(y)
    z = tf.square(debug_y)

    # Create a train op under the grad_debugger context.
    with grad_debugger:
      train_op = tf.compat.v1.train.GradientDescentOptimizer(z)

    # Now we can reflect through grad_debugger to get the gradient tensor
    # with respect to y.
    y_grad = grad_debugger.gradient_tensor(y)
    ```

    Args:
      input_tensor: the input `tf.Tensor` object whose related gradient tensors
        are to be registered with this `GradientsDebugger` instance when they
        are created, e.g., during `tf.gradients` calls or the construction
        of optimization (training) op that uses `tf.gradients`.

    Returns:
      A forwarded identity of `input_tensor`, as a `tf.Tensor`.

    Raises:
      ValueError: If an op with name that duplicates the gradient-debugging op
        already exists in the graph (highly unlikely).
    """
# TODO(cais): Allow overriding gradient.
# TODO(cais): Implement value_stack.
grad_debug_op_name = _tensor_to_grad_debug_op_name(input_tensor, self._uuid)
# pylint: disable=protected-access
identity_op = (
    gen_array_ops.debug_gradient_ref_identity
    if input_tensor.dtype._is_ref_dtype else
    gen_array_ops.debug_gradient_identity)
# pylint: enable=protected-access
debug_grad_identity = identity_op(input_tensor, name=grad_debug_op_name)
assert debug_grad_identity.dtype == input_tensor.dtype
if debug_grad_identity.op.name != grad_debug_op_name:
    raise ValueError(
        "The graph already contains an op named %s" % grad_debug_op_name)
exit(debug_grad_identity)
