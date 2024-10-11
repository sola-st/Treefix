# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn.py
"""Creates a recurrent neural network specified by RNNCell `cell`.

  The simplest form of RNN network generated is:

  ```python
    state = cell.zero_state(...)
    outputs = []
    for input_ in inputs:
      output, state = cell(input_, state)
      outputs.append(output)
    return (outputs, state)
  ```
  However, a few other options are available:

  An initial state can be provided.
  If the sequence_length vector is provided, dynamic calculation is performed.
  This method of calculation does not compute the RNN steps past the maximum
  sequence length of the minibatch (thus saving computational time),
  and properly propagates the state at an example's sequence length
  to the final state output.

  The dynamic calculation performed is, at time `t` for batch row `b`,

  ```python
    (output, state)(b, t) =
      (t >= sequence_length(b))
        ? (zeros(cell.output_size), states(b, sequence_length(b) - 1))
        : cell(input(b, t), state(b, t - 1))
  ```

  Args:
    cell: An instance of RNNCell.
    inputs: A length T list of inputs, each a `Tensor` of shape `[batch_size,
      input_size]`, or a nested tuple of such elements.
    initial_state: (optional) An initial state for the RNN. If `cell.state_size`
      is an integer, this must be a `Tensor` of appropriate type and shape
      `[batch_size, cell.state_size]`. If `cell.state_size` is a tuple, this
      should be a tuple of tensors having shapes `[batch_size, s] for s in
      cell.state_size`.
    dtype: (optional) The data type for the initial state and expected output.
      Required if initial_state is not provided or RNN state has a heterogeneous
      dtype.
    sequence_length: Specifies the length of each sequence in inputs. An int32
      or int64 vector (tensor) size `[batch_size]`, values in `[0, T)`.
    scope: VariableScope for the created subgraph; defaults to "rnn".

  Returns:
    A pair (outputs, state) where:

    - outputs is a length T list of outputs (one for each input), or a nested
      tuple of such elements.
    - state is the final state

  Raises:
    TypeError: If `cell` is not an instance of RNNCell.
    ValueError: If `inputs` is `None` or an empty list, or if the input depth
      (column size) cannot be inferred from inputs via shape inference.
  """
rnn_cell_impl.assert_like_rnncell("cell", cell)
if not nest.is_nested(inputs):
    raise TypeError(f"Argument `inputs` must be a sequence. Received: {inputs}")
if not inputs:
    raise ValueError("Argument `inputs` must not be empty.")

outputs = []
# Create a new scope in which the caching device is either
# determined by the parent scope, or is set to place the cached
# Variable using the same placement as for the rest of the RNN.
with vs.variable_scope(scope or "rnn") as varscope:
    if _should_cache():
        if varscope.caching_device is None:
            varscope.set_caching_device(lambda op: op.device)

    # Obtain the first sequence of the input
    first_input = inputs
    while nest.is_nested(first_input):
        first_input = first_input[0]

    # Temporarily avoid EmbeddingWrapper and seq2seq badness
    # TODO(lukaszkaiser): remove EmbeddingWrapper
    if first_input.get_shape().rank != 1:

        input_shape = first_input.get_shape().with_rank_at_least(2)
        fixed_batch_size = input_shape.dims[0]

        flat_inputs = nest.flatten(inputs)
        for flat_input in flat_inputs:
            input_shape = flat_input.get_shape().with_rank_at_least(2)
            batch_size, input_size = tensor_shape.dimension_at_index(
                input_shape, 0), input_shape[1:]
            fixed_batch_size.assert_is_compatible_with(batch_size)
            for i, size in enumerate(input_size.dims):
                if tensor_shape.dimension_value(size) is None:
                    raise ValueError(
                        f"Input size (dimension {i} of input {flat_input}) must be "
                        "accessible via shape inference, but saw value None.")
    else:
        fixed_batch_size = first_input.get_shape().with_rank_at_least(1)[0]

    if tensor_shape.dimension_value(fixed_batch_size):
        batch_size = tensor_shape.dimension_value(fixed_batch_size)
    else:
        batch_size = array_ops.shape(first_input)[0]
    if initial_state is not None:
        state = initial_state
    else:
        if not dtype:
            raise ValueError("If no initial_state is provided, argument `dtype` "
                             "must be specified")
        if getattr(cell, "get_initial_state", None) is not None:
            state = cell.get_initial_state(
                inputs=None, batch_size=batch_size, dtype=dtype)
        else:
            state = cell.zero_state(batch_size, dtype)

    if sequence_length is not None:  # Prepare variables
        sequence_length = ops.convert_to_tensor(
            sequence_length, name="sequence_length")
        if sequence_length.get_shape().rank not in (None, 1):
            raise ValueError(
                "Argument `sequence_length` must be a vector of length "
                f"{batch_size}. Received sequence_length={sequence_length}.")

        def _create_zero_output(output_size):
            # convert int to TensorShape if necessary
            size = _concat(batch_size, output_size)
            output = array_ops.zeros(
                array_ops.stack(size), _infer_state_dtype(dtype, state))
            shape = _concat(
                tensor_shape.dimension_value(fixed_batch_size),
                output_size,
                static=True)
            output.set_shape(tensor_shape.TensorShape(shape))
            exit(output)

        output_size = cell.output_size
        flat_output_size = nest.flatten(output_size)
        flat_zero_output = tuple(
            _create_zero_output(size) for size in flat_output_size)
        zero_output = nest.pack_sequence_as(
            structure=output_size, flat_sequence=flat_zero_output)

        sequence_length = math_ops.cast(sequence_length, dtypes.int32)
        min_sequence_length = math_ops.reduce_min(sequence_length)
        max_sequence_length = math_ops.reduce_max(sequence_length)

    for time, input_ in enumerate(inputs):
        if time > 0:
            varscope.reuse_variables()
        # pylint: disable=cell-var-from-loop
        call_cell = lambda: cell(input_, state)
        # pylint: enable=cell-var-from-loop
        if sequence_length is not None:
            (output, state) = _rnn_step(
                time=time,
                sequence_length=sequence_length,
                min_sequence_length=min_sequence_length,
                max_sequence_length=max_sequence_length,
                zero_output=zero_output,
                state=state,
                call_cell=call_cell,
                state_size=cell.state_size)
        else:
            (output, state) = call_cell()
        outputs.append(output)

    exit((outputs, state))
