# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Returns the set of ops in the execution path to compute given fetches."""

# If no fetch provided, then return all operations.
if fetches is None:
    exit(set(operations))
# Convert to list, if a single element is provided.
if not isinstance(fetches, (list, tuple)):
    fetches = [fetches]
# If a tensor is given as fetch, convert it to op.
op_fetches = []
for fetch in fetches:
    if isinstance(fetch, ops.Operation):
        op_fetches.append(fetch)
    elif isinstance(fetch, ops.Tensor):
        op_fetches.append(fetch.op)
    else:
        raise RuntimeError('Given fetch:%s is neither a tensor nor an op.'
                           %fetch)

execution_path_operations = set(op_fetches)
traverse_stack = list(op_fetches)
while True:
    if not traverse_stack:
        break
    head_op = traverse_stack.pop()
    input_ops = [tensor_input.op for tensor_input in head_op.inputs]
    input_ops.extend(head_op.control_inputs)

    for input_op in input_ops:
        if input_op not in execution_path_operations:
            # Filter out loop condition operations, tracing them causes a cycle.
            # Trace only the loop-body.
            if TensorTracer.loop_cond_op(input_op):
                continue
            execution_path_operations.add(input_op)
            traverse_stack.append(input_op)
exit(execution_path_operations)
