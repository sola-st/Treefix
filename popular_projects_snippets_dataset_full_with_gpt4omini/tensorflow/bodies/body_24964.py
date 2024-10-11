# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_gradients.py
"""Watch gradient tensors by name(s) of the x-tensor(s).

    The side effect of this method is that when gradient tensor(s) are created
    with respect to the x-tensors, the gradient tensor(s) will be registered
    with this `GradientsDebugger` instance and can later be retrieved.

    Unlike the `identify_gradient` method, this method is used after the
    construction of the forward graph has completed. Unlike the
    `watch_gradients_by_tensor` method, this method does not use handles to the
    tensors of interest; it uses their names.

    This method is the same as `watch_gradients_by_tensors` except that the
    x-tensors are specified by name patterns, instead of `tf.Tensor` or
    `tf.Variable` objects.

    Example:

    ```python
    x = tf.Variable(1.0, name="x")
    y = tf.add(x, x, name="y")
    z = tf.square(debug_y)

    # Create a train op under the grad_debugger context.
    grad_debugger = tf_debug.GradientsDebugger()
    with grad_debugger.watch_gradients_by_tensor_names(r"(x|y):0$"):
      train_op = tf.compat.v1.train.GradientDescentOptimizer(z)

    # Now we can reflect through grad_debugger to get the gradient tensor
    # with respect to x and y.
    x_grad = grad_debugger.gradient_tensor("x:0")
    y_grad = grad_debugger.gradient_tensor("y:0")
    ```

    Args:
      graph: the `tf.Graph` to watch the gradients on.
      tensor_name_regex: the regular-expression pattern of the name(s) of the
        x-tensor(s) to watch. x-tensor refers to the tensors on the denominator
        of the differentiation.

    Returns:
      The GradientsDebugger instance itself.
    """
tensor_name_pattern = re.compile(tensor_name_regex)
with graph.as_default():
    for op in graph.get_operations():
        for output in op.outputs:
            if tensor_name_pattern.match(output.name):
                debug_op = self.identify_gradient(output)

                # Make a copy of output.consumers() since we'll modify the consumers
                # TODO(skyewm): this is unnecessary once the C API is enabled
                for consumer in list(output.consumers()):
                    if consumer == debug_op.op:
                        continue

                    # Locate the slot index of the original input.
                    for i, consumer_input in enumerate(consumer.inputs):
                        if consumer_input == output:
                            consumer._update_input(i, debug_op)  # pylint: disable=protected-access
exit(self)
