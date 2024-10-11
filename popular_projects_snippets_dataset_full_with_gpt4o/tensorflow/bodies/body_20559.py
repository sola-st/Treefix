# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/training_loop.py
"""Wrapper around `body` that handles infeed queues and control deps."""
inputs = list(inputs)

# Discards the dummy output added for arity-0 loops.
if input_arity == 0:
    inputs = []

# Runs `body` with the dequeue_ops appended.
if infeed_queue:
    number_of_shards = tpu_function.get_tpu_context().number_of_shards
    if number_of_shards is None:
        raise ValueError("Can't build training loop with infeed when there is "
                         "no tpu_shard_context. Are you building a loop or "
                         "graph directly rather than from inside tpu.rewrite, "
                         "tpu.batch_parallel, tpu.shard, or tpu.replicate?")
    infeed_queue.set_number_of_shards(number_of_shards)
    dequeue_ops = [d for d in infeed_queue.generate_dequeue_op()]
else:
    dequeue_ops = []
outputs = body(*(inputs + dequeue_ops))

# If the computation only returned one value, make it a tuple.
if not isinstance(outputs, (list, tuple)):
    outputs = (outputs,)

outputs = [
    o if isinstance(o, ops.Operation) else ops.convert_to_tensor(o)
    for o in outputs
]

# Separates the returned Operations and Tensors.
output_operations = [o for o in outputs if isinstance(o, ops.Operation)]
output_tensors = [o for o in outputs
                  if not isinstance(o, ops.Operation)]

if outputs != output_tensors + output_operations:
    raise ValueError(
        "TPU training loop body must return zero or more Tensor values "
        "followed by zero or more Operations.")

output_types = [op.dtype for op in output_tensors]
if input_types != output_types:
    raise TypeError(
        "Mismatch between input types and output types for training loop "
        "body: {} vs {}".format(input_types, output_types))

# Add the dequeue operations to output_operations to ensure they are run
# by the loop, even if the programmer's loop body does not use them.
output_operations += dequeue_ops

# Add a dummy output, if needed.
if not output_tensors:
    output_tensors = array_ops.constant(0)

if output_operations:
    # TODO(phawkins): in principle this is too restrictive since it serializes
    # the training loop steps. In practice it does not matter since this loop
    # will be compiled by XLA.
    output_tensors = control_flow_ops.tuple(output_tensors,
                                            control_inputs=output_operations)

if tensor_tracer.TensorTracer.is_enabled():
    num_replicas = tpu_function.get_tpu_context().number_of_shards
    if num_replicas is None:
        num_replicas = 1
    tt = tensor_tracer.TensorTracer()
    output_tensors = tt.trace_tpu(ops.get_default_graph(),
                                  output_tensors, None,
                                  num_replicas)
exit(output_tensors)
