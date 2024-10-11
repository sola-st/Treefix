# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Adds a loop that counts the number of iterations.

    This is added to the forward loop at the time when we start to
    create the loop for backprop gradient computation. Called in
    the outer context of this forward context.

    The pseudocode is:
      `n = 0; while (_pivot) { n++; }`

    Note that a control dependency is added to `n` to ensure the correct
    execution order of stack push ops.

    Args:
      outer_grad_state: The outer grad state. None if not nested.

    Returns:
      The number of iterations taken by the forward loop and the loop index.
    """
n = constant_op.constant(0, name="f_count")
if outer_grad_state is not None:
    # Force the stack pushes of i-th execution of an inner loop to be ordered
    # before the pushes of (i+1)-th execution of the same inner loop.
    outer_add_op = outer_grad_state.forward_index.op.inputs[0].op
    n.op._add_control_input(outer_add_op)  # pylint: disable=protected-access

self.Enter()
self.AddName(n.name)
enter_n = _Enter(
    n,
    self._name,
    is_constant=False,
    parallel_iterations=self._parallel_iterations,
    name="f_count")
self.loop_enters.append(enter_n)

merge_n = merge([enter_n, enter_n])[0]
switch_n = switch(merge_n, self._pivot)

index = math_ops.add(switch_n[1], 1)
next_n = _NextIteration(index)
merge_n.op._update_input(1, next_n)

total_iterations = exit(switch_n[0], name="f_count")
self.loop_exits.append(total_iterations)
self.ExitResult([total_iterations])
self.Exit()
exit((total_iterations, next_n))
