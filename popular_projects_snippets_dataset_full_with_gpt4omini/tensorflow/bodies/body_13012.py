# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn.py
"""Creates an `RNN` specified by RNNCell `cell` and loop function `loop_fn`.

  **NOTE: This method is still in testing, and the API may change.**

  This function is a more primitive version of `dynamic_rnn` that provides
  more direct access to the inputs each iteration.  It also provides more
  control over when to start and finish reading the sequence, and
  what to emit for the output.

  For example, it can be used to implement the dynamic decoder of a seq2seq
  model.

  Instead of working with `Tensor` objects, most operations work with
  `TensorArray` objects directly.

  The operation of `raw_rnn`, in pseudo-code, is basically the following:

  ```python
  time = tf.constant(0, dtype=tf.int32)
  (finished, next_input, initial_state, emit_structure, loop_state) = loop_fn(
      time=time, cell_output=None, cell_state=None, loop_state=None)
  emit_ta = TensorArray(dynamic_size=True, dtype=initial_state.dtype)
  state = initial_state
  while not all(finished):
    (output, cell_state) = cell(next_input, state)
    (next_finished, next_input, next_state, emit, loop_state) = loop_fn(
        time=time + 1, cell_output=output, cell_state=cell_state,
        loop_state=loop_state)
    # Emit zeros and copy forward state for minibatch entries that are finished.
    state = tf.where(finished, state, next_state)
    emit = tf.where(finished, tf.zeros_like(emit_structure), emit)
    emit_ta = emit_ta.write(time, emit)
    # If any new minibatch entries are marked as finished, mark these.
    finished = tf.logical_or(finished, next_finished)
    time += 1
  return (emit_ta, state, loop_state)
  ```

  with the additional properties that output and state may be (possibly nested)
  tuples, as determined by `cell.output_size` and `cell.state_size`, and
  as a result the final `state` and `emit_ta` may themselves be tuples.

  A simple implementation of `dynamic_rnn` via `raw_rnn` looks like this:

  ```python
  inputs = tf.compat.v1.placeholder(shape=(max_time, batch_size, input_depth),
                          dtype=tf.float32)
  sequence_length = tf.compat.v1.placeholder(shape=(batch_size,),
  dtype=tf.int32)
  inputs_ta = tf.TensorArray(dtype=tf.float32, size=max_time)
  inputs_ta = inputs_ta.unstack(inputs)

  cell = tf.compat.v1.nn.rnn_cell.LSTMCell(num_units)

  def loop_fn(time, cell_output, cell_state, loop_state):
    emit_output = cell_output  # == None for time == 0
    if cell_output is None:  # time == 0
      next_cell_state = cell.zero_state(batch_size, tf.float32)
    else:
      next_cell_state = cell_state
    elements_finished = (time >= sequence_length)
    finished = tf.reduce_all(elements_finished)
    next_input = tf.cond(
        finished,
        lambda: tf.zeros([batch_size, input_depth], dtype=tf.float32),
        lambda: inputs_ta.read(time))
    next_loop_state = None
    return (elements_finished, next_input, next_cell_state,
            emit_output, next_loop_state)

  outputs_ta, final_state, _ = raw_rnn(cell, loop_fn)
  outputs = outputs_ta.stack()
  ```

  Args:
    cell: An instance of RNNCell.
    loop_fn: A callable that takes inputs `(time, cell_output, cell_state,
      loop_state)` and returns the tuple `(finished, next_input,
      next_cell_state, emit_output, next_loop_state)`. Here `time` is an int32
      scalar `Tensor`, `cell_output` is a `Tensor` or (possibly nested) tuple of
      tensors as determined by `cell.output_size`, and `cell_state` is a
      `Tensor` or (possibly nested) tuple of tensors, as determined by the
      `loop_fn` on its first call (and should match `cell.state_size`).
      The outputs are: `finished`, a boolean `Tensor` of
      shape `[batch_size]`, `next_input`: the next input to feed to `cell`,
      `next_cell_state`: the next state to feed to `cell`,
      and `emit_output`: the output to store for this iteration.  Note that
        `emit_output` should be a `Tensor` or (possibly nested) tuple of tensors
        which is aggregated in the `emit_ta` inside the `while_loop`. For the
        first call to `loop_fn`, the `emit_output` corresponds to the
        `emit_structure` which is then used to determine the size of the
        `zero_tensor` for the `emit_ta` (defaults to `cell.output_size`). For
        the subsequent calls to the `loop_fn`, the `emit_output` corresponds to
        the actual output tensor that is to be aggregated in the `emit_ta`. The
        parameter `cell_state` and output `next_cell_state` may be either a
        single or (possibly nested) tuple of tensors.  The parameter
        `loop_state` and output `next_loop_state` may be either a single or
        (possibly nested) tuple of `Tensor` and `TensorArray` objects.  This
        last parameter may be ignored by `loop_fn` and the return value may be
        `None`.  If it is not `None`, then the `loop_state` will be propagated
        through the RNN loop, for use purely by `loop_fn` to keep track of its
        own state. The `next_loop_state` parameter returned may be `None`.  The
        first call to `loop_fn` will be `time = 0`, `cell_output = None`,
      `cell_state = None`, and `loop_state = None`.  For this call: The
        `next_cell_state` value should be the value with which to initialize the
        cell's state.  It may be a final state from a previous RNN or it may be
        the output of `cell.zero_state()`.  It should be a (possibly nested)
        tuple structure of tensors. If `cell.state_size` is an integer, this
        must be a `Tensor` of appropriate type and shape `[batch_size,
        cell.state_size]`. If `cell.state_size` is a `TensorShape`, this must be
        a `Tensor` of appropriate type and shape `[batch_size] +
        cell.state_size`. If `cell.state_size` is a (possibly nested) tuple of
        ints or `TensorShape`, this will be a tuple having the corresponding
        shapes. The `emit_output` value may be either `None` or a (possibly
        nested) tuple structure of tensors, e.g., `(tf.zeros(shape_0,
        dtype=dtype_0), tf.zeros(shape_1, dtype=dtype_1))`. If this first
        `emit_output` return value is `None`, then the `emit_ta` result of
        `raw_rnn` will have the same structure and dtypes as `cell.output_size`.
        Otherwise `emit_ta` will have the same structure, shapes (prepended with
        a `batch_size` dimension), and dtypes as `emit_output`.  The actual
        values returned for `emit_output` at this initializing call are ignored.
        Note, this emit structure must be consistent across all time steps.
    parallel_iterations: (Default: 32).  The number of iterations to run in
      parallel.  Those operations which do not have any temporal dependency and
      can be run in parallel, will be.  This parameter trades off time for
      space.  Values >> 1 use more memory but take less time, while smaller
      values use less memory but computations take longer.
    swap_memory: Transparently swap the tensors produced in forward inference
      but needed for back prop from GPU to CPU.  This allows training RNNs which
      would typically not fit on a single GPU, with very minimal (or no)
      performance penalty.
    scope: VariableScope for the created subgraph; defaults to "rnn".

  Returns:
    A tuple `(emit_ta, final_state, final_loop_state)` where:

    `emit_ta`: The RNN output `TensorArray`.
       If `loop_fn` returns a (possibly nested) set of Tensors for
       `emit_output` during initialization, (inputs `time = 0`,
       `cell_output = None`, and `loop_state = None`), then `emit_ta` will
       have the same structure, dtypes, and shapes as `emit_output` instead.
       If `loop_fn` returns `emit_output = None` during this call,
       the structure of `cell.output_size` is used:
       If `cell.output_size` is a (possibly nested) tuple of integers
       or `TensorShape` objects, then `emit_ta` will be a tuple having the
       same structure as `cell.output_size`, containing TensorArrays whose
       elements' shapes correspond to the shape data in `cell.output_size`.

    `final_state`: The final cell state.  If `cell.state_size` is an int, this
      will be shaped `[batch_size, cell.state_size]`.  If it is a
      `TensorShape`, this will be shaped `[batch_size] + cell.state_size`.
      If it is a (possibly nested) tuple of ints or `TensorShape`, this will
      be a tuple having the corresponding shapes.

    `final_loop_state`: The final loop state as returned by `loop_fn`.

  Raises:
    TypeError: If `cell` is not an instance of RNNCell, or `loop_fn` is not
      a `callable`.
  """
rnn_cell_impl.assert_like_rnncell("cell", cell)

if not callable(loop_fn):
    raise TypeError("Argument `loop_fn` must be a callable. Received: "
                    f"{loop_fn}.")

parallel_iterations = parallel_iterations or 32

# Create a new scope in which the caching device is either
# determined by the parent scope, or is set to place the cached
# Variable using the same placement as for the rest of the RNN.
with vs.variable_scope(scope or "rnn") as varscope:
    if _should_cache():
        if varscope.caching_device is None:
            varscope.set_caching_device(lambda op: op.device)

    time = constant_op.constant(0, dtype=dtypes.int32)
    (elements_finished, next_input,
     initial_state, emit_structure, init_loop_state) = loop_fn(
         time, None, None, None)  # time, cell_output, cell_state, loop_state
    flat_input = nest.flatten(next_input)

    # Need a surrogate loop state for the while_loop if none is available.
    loop_state = (
        init_loop_state if init_loop_state is not None else
        constant_op.constant(0, dtype=dtypes.int32))

    input_shape = [input_.get_shape() for input_ in flat_input]
    static_batch_size = tensor_shape.dimension_at_index(input_shape[0], 0)

    for input_shape_i in input_shape:
        # Static verification that batch sizes all match
        static_batch_size.assert_is_compatible_with(
            tensor_shape.dimension_at_index(input_shape_i, 0))

    batch_size = tensor_shape.dimension_value(static_batch_size)
    const_batch_size = batch_size
    if batch_size is None:
        batch_size = array_ops.shape(flat_input[0])[0]

    nest.assert_same_structure(initial_state, cell.state_size)
    state = initial_state
    flat_state = nest.flatten(state)
    flat_state = [ops.convert_to_tensor(s) for s in flat_state]
    state = nest.pack_sequence_as(structure=state, flat_sequence=flat_state)

    if emit_structure is not None:
        flat_emit_structure = nest.flatten(emit_structure)
        flat_emit_size = [
            emit.shape if emit.shape.is_fully_defined() else array_ops.shape(emit)
            for emit in flat_emit_structure
        ]
        flat_emit_dtypes = [emit.dtype for emit in flat_emit_structure]
    else:
        emit_structure = cell.output_size
        flat_emit_size = nest.flatten(emit_structure)
        flat_emit_dtypes = [flat_state[0].dtype] * len(flat_emit_size)

    flat_emit_ta = [
        tensor_array_ops.TensorArray(
            dtype=dtype_i,
            dynamic_size=True,
            element_shape=(tensor_shape.TensorShape([
                const_batch_size
            ]).concatenate(_maybe_tensor_shape_from_tensor(size_i))),
            size=0,
            name="rnn_output_%d" % i)
        for i, (dtype_i,
                size_i) in enumerate(zip(flat_emit_dtypes, flat_emit_size))
    ]
    emit_ta = nest.pack_sequence_as(
        structure=emit_structure, flat_sequence=flat_emit_ta)
    flat_zero_emit = [
        array_ops.zeros(_concat(batch_size, size_i), dtype_i)
        for size_i, dtype_i in zip(flat_emit_size, flat_emit_dtypes)
    ]
    zero_emit = nest.pack_sequence_as(
        structure=emit_structure, flat_sequence=flat_zero_emit)

    def condition(unused_time, elements_finished, *_):
        exit(math_ops.logical_not(math_ops.reduce_all(elements_finished)))

    def body(time, elements_finished, current_input, emit_ta, state,
             loop_state):
        """Internal while loop body for raw_rnn.

      Args:
        time: time scalar.
        elements_finished: batch-size vector.
        current_input: possibly nested tuple of input tensors.
        emit_ta: possibly nested tuple of output TensorArrays.
        state: possibly nested tuple of state tensors.
        loop_state: possibly nested tuple of loop state tensors.

      Returns:
        Tuple having the same size as Args but with updated values.
      """
        (next_output, cell_state) = cell(current_input, state)

        nest.assert_same_structure(state, cell_state)
        nest.assert_same_structure(cell.output_size, next_output)

        next_time = time + 1
        (next_finished, next_input, next_state, emit_output,
         next_loop_state) = loop_fn(next_time, next_output, cell_state,
                                    loop_state)

        nest.assert_same_structure(state, next_state)
        nest.assert_same_structure(current_input, next_input)
        nest.assert_same_structure(emit_ta, emit_output)

        # If loop_fn returns None for next_loop_state, just reuse the
        # previous one.
        loop_state = loop_state if next_loop_state is None else next_loop_state

        def _copy_some_through(current, candidate):
            """Copy some tensors through via array_ops.where."""

            def copy_fn(cur_i, cand_i):
                # TensorArray and scalar get passed through.
                if isinstance(cur_i, tensor_array_ops.TensorArray):
                    exit(cand_i)
                if cur_i.shape.rank == 0:
                    exit(cand_i)
                # Otherwise propagate the old or the new value.
                with ops.colocate_with(cand_i):
                    exit(array_ops.where(elements_finished, cur_i, cand_i))

            exit(nest.map_structure(copy_fn, current, candidate))

        emit_output = _copy_some_through(zero_emit, emit_output)
        next_state = _copy_some_through(state, next_state)

        emit_ta = nest.map_structure(lambda ta, emit: ta.write(time, emit),
                                     emit_ta, emit_output)

        elements_finished = math_ops.logical_or(elements_finished, next_finished)

        exit((next_time, elements_finished, next_input, emit_ta, next_state,
                loop_state))

    returned = control_flow_ops.while_loop(
        condition,
        body,
        loop_vars=[
            time, elements_finished, next_input, emit_ta, state, loop_state
        ],
        parallel_iterations=parallel_iterations,
        swap_memory=swap_memory)

    (emit_ta, final_state, final_loop_state) = returned[-3:]

    if init_loop_state is None:
        final_loop_state = None

    exit((emit_ta, final_state, final_loop_state))
