# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Add the backprop loop that controls the iterations.

    This is added to the backprop loop. It is used to control the loop
    termination of the backprop loop. Called in the outer context of
    this grad context.

    The pseudocode is:
      `n = count; while (n >= 1) { n--; }`

    Note that a control dependency is added to `final_zero` to ensure the
    correct execution order of stack pop ops.

    Args:
      count: The number of iterations for backprop.
      outer_grad_state: The outer grad state. None if not nested.

    Returns:
      The loop index.
    """
in_separate_functions = count.graph is not ops.get_default_graph()
if in_separate_functions:
    # Brings the count into this graph
    count = array_ops.identity(count)
else:
    # TODO(apassos) XLA expects this constant to be created outside the loop,
    # so doing that for now.
    one = constant_op.constant(1, name="b_count")

self.Enter()
self.AddName(count.name)
enter_count = _Enter(
    count,
    self._name,
    is_constant=False,
    parallel_iterations=self._parallel_iterations,
    name="b_count")
self.loop_enters.append(enter_count)

merge_count = merge([enter_count, enter_count])[0]
self._pivot_for_pred = merge_count

if in_separate_functions:
    one = constant_op.constant(1, name="b_count")
pred = math_ops.greater_equal(merge_count, one)
self._pivot = loop_cond(pred, name="b_count")
switch_count = switch(merge_count, self._pivot)

index = math_ops.subtract(switch_count[1], one)
self._pivot_for_body = index
next_count = _NextIteration(index)
merge_count.op._update_input(1, next_count)

final_zero = exit(switch_count[0], name="b_count")
self.loop_exits.append(final_zero)
if outer_grad_state is not None:
    # Force the stack pops of i-th execution of an inner loop to be ordered
    # before the pops of (i+1)-th execution of the same inner loop.
    # pylint: disable=protected-access
    outer_grad_state.grad_sync._add_control_input(final_zero.op)
    # pylint: enable=protected-access

self.ExitResult([final_zero])
self.Exit()
exit(next_count)
