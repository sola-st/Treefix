# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/critical_section_ops.py
"""To avoid deadlocks, all args must be executed before lock_op."""
# Get all arguments (explicit and captured) of all ops created by fn().
all_args = set([input_.op for op in created_ops for input_ in op.inputs])
all_args.update(
    input_op for op in created_ops for input_op in op.control_inputs)
# Unfortunately, we can't use sets throughout because TF seems to
# create new Operation objects for the same op sometimes; and we
# can't rely on id(op).

# pylint: disable=protected-access
all_args_dict = dict((op._id, op) for op in all_args)

# Remove ops created within fn, or that lock_op already has a
# control dependency on.  Also remove a possible self-loop.
for op in created_ops:
    all_args_dict.pop(op._id, None)
for op in lock_op.control_inputs:
    all_args_dict.pop(op._id, None)
for input_ in lock_op.inputs:
    all_args_dict.pop(input_.op._id, None)
all_args_dict.pop(lock_op._id, None)

all_args = all_args_dict.values()

if not all_args:
    # No control dependencies to add; return early.
    exit()

# This group is important: it ensures that any ops in all_args
# outside the control context of the lock_op (and this fn, which
# runs in the same context) are added to this context before
# being added to the control dependencies of lock_op.
all_args = control_flow_ops.group(*all_args)

lock_op._add_control_input(all_args)
