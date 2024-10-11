# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Add an accumulation loop for every loop invariant.

    This is added to the backprop loop. It is used to accumulate partial
    gradients within each loop iteration. Called when in the gradient while
    context.

    The pseudocode is:
      ```
      acc = 0.0;
      while (_pivot) {
        acc += grad;
      }
      ```

    Args:
      op: The Enter op for a loop invariant.
      grad: The partial gradient of an iteration for a loop invariant.

    Returns:
      The gradient for a loop invariant.
    """
self.Exit()
# Create a zeros tensor with the right shape for acc. If we don't
# know the full shape statically, we will have to get the shape
# dynamically from the forward inference. Getting the shape right
# for the zeros is only needed for the base case when the loop exits
# without running any iterations.
shape = grad.get_shape()
if shape.is_fully_defined():
    if self.outer_context:
        self.outer_context.Enter()
    acc = constant_op.constant(0, grad.dtype, shape=shape, name="b_acc")
    if self.outer_context:
        self.outer_context.Exit()
else:
    value = op.inputs[0]
    if (isinstance(self.outer_context, WhileContext) and
        self.outer_context.grad_state is not None):
        # We are in a nested while loop.
        forward_ctxt = self.grad_state.forward_context
        forward_ctxt.outer_context.Enter()
        zeros_shape = array_ops.shape_internal(value, optimize=False)
        forward_ctxt.outer_context.Exit()
        outer_grad_state = self.grad_state.outer_grad_state
        history_zeros_shape = outer_grad_state.AddForwardAccumulator(
            zeros_shape)
        self.outer_context.Enter()
        real_shape = outer_grad_state.AddBackpropAccumulatedValue(
            history_zeros_shape, zeros_shape)
        acc = array_ops.zeros(real_shape, grad.dtype)
        self.outer_context.Exit()
    else:
        if self.outer_context:
            self.outer_context.Enter()
        zeros_shape = array_ops.shape_internal(value, optimize=False)
        acc = array_ops.zeros(zeros_shape, grad.dtype)
        if self.outer_context:
            self.outer_context.Exit()

self.Enter()
self.AddName(acc.name)
enter_acc = _Enter(
    acc,
    self._name,
    is_constant=False,
    parallel_iterations=self._parallel_iterations,
    name="b_acc")
self.loop_enters.append(enter_acc)

merge_acc = merge([enter_acc, enter_acc], name="b_acc")[0]
switch_acc_false, switch_acc_true = switch(merge_acc, self._pivot)

add_acc = math_ops.add(switch_acc_true, grad)
next_acc = _NextIteration(add_acc)
merge_acc.op._update_input(1, next_acc)  # pylint: disable=protected-access

result_acc = exit(switch_acc_false, name="b_acc")
self.loop_exits.append(result_acc)
self.ExitResult([result_acc])
exit(result_acc)
