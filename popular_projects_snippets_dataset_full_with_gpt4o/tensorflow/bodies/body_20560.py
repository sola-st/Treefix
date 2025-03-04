# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/training_loop.py
"""Builds a training loop for TPUs.

  The set of loop-carried tensors corresponds to `inputs`.  Both
  `condition` and `body` take the current value of the loop-carried
  tensors. 'body' additionally takes a tuple of infeed from
  infeed_queue if infeed_queue is not None. `condition` must return a
  single boolean value that determines whether iteration
  continues. `body` must return an updated list of values for the
  loop-carried tensors.

  Args:
    condition: a Python function that builds the loop condition.
    body: a Python function that builds the loop body.
    inputs: a list of initial values passed into the training loop, or None
      (equivalent to an empty list).
    infeed_queue: if not None, the infeed queue from which to append a tuple of
      arguments as inputs to condition.
    name: (Deprecated) Does nothing.

  Returns:
    The final values of the loop-carried tensors.

  Raises:
    TypeError: if body or condition has the wrong signature.
  """
del name
# Converts inputs to Tensors.
inputs = [] if inputs is None else [ops.convert_to_tensor(x) for
                                    x in inputs]
input_types = [x.dtype for x in inputs]
input_arity = len(inputs)

body_arg_error = xla.check_function_argument_count(
    body, input_arity, infeed_queue)
if body_arg_error is not None:
    if infeed_queue is None:
        raise TypeError(
            f"Supplied loop body function cannot be called with the specified "
            f"inputs. You specified {input_arity} inputs: {[i.name for i in inputs]}, but the loop body needs {body_arg_error}"
        )
    else:
        raise TypeError(
            f"Supplied loop body function cannot be called with the specified "
            f"inputs. You specified {input_arity} inputs: {[i.name for i in inputs]} and {infeed_queue.number_of_tuple_elements} additional inputs from "
            f"infeed, but the computation needs {body_arg_error}")
condition_arg_error = xla.check_function_argument_count(
    condition, input_arity, None)
if condition_arg_error is not None:
    if infeed_queue is None:
        raise TypeError(
            f"Supplied loop condition function cannot be called with the "
            f"specified inputs. You specified {input_arity} inputs: {[i.name for i in inputs]}, but the loop "
            f"condition needs {condition_arg_error}")
    else:
        raise TypeError(
            f"Supplied loop condition function cannot be called with the "
            f"specified inputs. You specified {input_arity} inputs: {[i.name for i in inputs]}, but the loop "
            f"condition needs {condition_arg_error}. Note that infeed is not passed to the loop condition."
        )

def condition_wrapper(*inputs):
    # Discards the dummy output added for arity-0 loops.
    if input_arity == 0:
        inputs = []
    exit(condition(*inputs))

def body_wrapper(*inputs):
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

# If the body has arity 0, add a dummy loop-carried value to which we can add
# control dependencies from any side-effecting operations.
if input_arity == 0:
    inputs = [array_ops.constant(0)]
exit(control_flow_ops.while_loop(
    condition_wrapper, body_wrapper, inputs, name="", parallel_iterations=1))
