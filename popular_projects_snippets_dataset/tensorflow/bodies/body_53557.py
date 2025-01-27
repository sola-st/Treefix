# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns a context manager that specifies control dependencies.

    Use with the `with` keyword to specify that all operations constructed
    within the context should have control dependencies on
    `control_inputs`. For example:

    ```python
    with g.control_dependencies([a, b, c]):
      # `d` and `e` will only run after `a`, `b`, and `c` have executed.
      d = ...
      e = ...
    ```

    Multiple calls to `control_dependencies()` can be nested, and in
    that case a new `Operation` will have control dependencies on the union
    of `control_inputs` from all active contexts.

    ```python
    with g.control_dependencies([a, b]):
      # Ops constructed here run after `a` and `b`.
      with g.control_dependencies([c, d]):
        # Ops constructed here run after `a`, `b`, `c`, and `d`.
    ```

    You can pass None to clear the control dependencies:

    ```python
    with g.control_dependencies([a, b]):
      # Ops constructed here run after `a` and `b`.
      with g.control_dependencies(None):
        # Ops constructed here run normally, not waiting for either `a` or `b`.
        with g.control_dependencies([c, d]):
          # Ops constructed here run after `c` and `d`, also not waiting
          # for either `a` or `b`.
    ```

    *N.B.* The control dependencies context applies *only* to ops that
    are constructed within the context. Merely using an op or tensor
    in the context does not add a control dependency. The following
    example illustrates this point:

    ```python
    # WRONG
    def my_func(pred, tensor):
      t = tf.matmul(tensor, tensor)
      with tf.control_dependencies([pred]):
        # The matmul op is created outside the context, so no control
        # dependency will be added.
        return t

    # RIGHT
    def my_func(pred, tensor):
      with tf.control_dependencies([pred]):
        # The matmul op is created in the context, so a control dependency
        # will be added.
        return tf.matmul(tensor, tensor)
    ```

    Also note that though execution of ops created under this scope will trigger
    execution of the dependencies, the ops created under this scope might still
    be pruned from a normal tensorflow graph. For example, in the following
    snippet of code the dependencies are never executed:

    ```python
      loss = model.loss()
      with tf.control_dependencies(dependencies):
        loss = loss + tf.constant(1)  # note: dependencies ignored in the
                                      # backward pass
      return tf.gradients(loss, model.variables)
    ```

    This is because evaluating the gradient graph does not require evaluating
    the constant(1) op created in the forward pass.

    Args:
      control_inputs: A list of `Operation` or `Tensor` objects which must be
        executed or computed before running the operations defined in the
        context.  Can also be `None` to clear the control dependencies.

    Returns:
     A context manager that specifies control dependencies for all
     operations constructed within the context.

    Raises:
      TypeError: If `control_inputs` is not a list of `Operation` or
        `Tensor` objects.
    """
if control_inputs is None:
    exit(self._ControlDependenciesController(self, None))
# First convert the inputs to ops, and deduplicate them.
# NOTE(mrry): Other than deduplication, we do not currently track direct
#   or indirect dependencies between control_inputs, which may result in
#   redundant control inputs.
control_ops = []
current = self._current_control_dependencies()
for c in control_inputs:
    # The hasattr(handle) is designed to match ResourceVariables. This is so
    # control dependencies on a variable or on an unread variable don't
    # trigger reads.
    if (isinstance(c, IndexedSlices) or
        (hasattr(c, "_handle") and hasattr(c, "op"))):
        c = c.op
    c = self.as_graph_element(c)
    if isinstance(c, Tensor):
        c = c.op
    elif not isinstance(c, Operation):
        raise TypeError("Control input must be Operation or Tensor: %s" % c)
    if c not in current:
        control_ops.append(c)
        current.add(c)
        # Mark this op with an attribute indicating that it is used as a manual
        # control dep in order to allow tracking how common utilization of
        # manual control deps in graphs run through the MLIR Bridge are. See
        # go/manual-control-dependencies-bridge for details.
        # pylint: disable=protected-access
        c._set_attr("_has_manual_control_dependencies",
                    attr_value_pb2.AttrValue(b=True))
        # pylint: enable=protected-access
exit(self._ControlDependenciesController(self, control_ops))
