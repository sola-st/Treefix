# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent_v2.py
"""LSTM with either CuDNN or ROCm implementation which is only available for GPU.

  Note that currently only right padded data is supported, or the result will be
  polluted by the unmasked data which should be filtered.

  Args:
    inputs: Input tensor of LSTM layer.
    init_h: Initial state tensor for the cell output.
    init_c: Initial state tensor for the cell hidden state.
    kernel: Weights for cell kernel.
    recurrent_kernel: Weights for cell recurrent kernel.
    bias: Weights for cell kernel bias and recurrent bias. Only recurrent bias
      is used in this case.
    mask: Boolean tensor for mask out the steps within sequence.
      An individual `True` entry indicates that the corresponding timestep
      should be utilized, while a `False` entry indicates that the corresponding
      timestep should be ignored.
    time_major: Boolean, whether the inputs are in the format of [time, batch,
      feature] or [batch, time, feature].
    go_backwards: Boolean (default False). If True, process the input sequence
      backwards and return the reversed sequence.
    sequence_lengths: The lengths of all sequences coming from a variable length
      input, such as ragged tensors. If the input has a fixed timestep size,
      this should be None.

  Returns:
    last_output: Output tensor for the last timestep, which has shape
      [batch, units].
    outputs: Output tensor for all timesteps, which has shape
      [batch, time, units].
    state_0: The cell output, which has same shape as init_h.
    state_1: The cell hidden state, which has same shape as init_c.
    runtime: Constant string tensor which indicate real runtime hardware. This
      value is for testing purpose and should not be used by user.
  """
if not time_major and mask is None:
    inputs = array_ops.transpose(inputs, perm=(1, 0, 2))
    seq_axis, batch_axis = (0, 1)
else:
    seq_axis, batch_axis = (0, 1) if time_major else (1, 0)
# For init_h and init_c, cuDNN expects one more dim of num_layers before or
# after batch dim for time major or batch major inputs respectively
init_h = array_ops.expand_dims(init_h, axis=seq_axis)
init_c = array_ops.expand_dims(init_c, axis=seq_axis)

weights = array_ops.split(kernel, 4, axis=1)
weights += array_ops.split(recurrent_kernel, 4, axis=1)
# CuDNN has an extra set of bias for inputs, we disable them (setting to 0),
# so that mathematically it is same as the canonical LSTM implementation.
full_bias = array_ops.concat((array_ops.zeros_like(bias), bias), 0)

if sysconfig.get_build_info()['is_rocm_build']:
    # ROCm MIOpen's weight sequence for LSTM is different from both canonical
    # and Cudnn format
    # MIOpen: [i, f, o, c] Cudnn/Canonical: [i, f, c, o]
    # i is input gate weights.
    # f is forget gate weights.
    # o is output gate weights.
    # c is cell gate weights.
    weights = [weights[x] for x in (0, 1, 3, 2, 4, 5, 7, 6)]
    # full_bias is a tensor of shape (8*n,)
    full_bias = array_ops.split(full_bias, 8, axis=0)
    full_bias = [full_bias[x] for x in (0, 1, 3, 2, 4, 5, 7, 6)]

params = _canonical_to_params(
    weights=weights,
    biases=array_ops.split(full_bias, 8),
    shape=constant_op.constant([-1]),
    transpose_weights=True)

if mask is not None:
    sequence_lengths = calculate_sequence_by_mask(mask, time_major)

if sequence_lengths is not None:
    if go_backwards:
        # Three reversals are required. E.g.,
        # normal input = [1, 2, 3, 0, 0]  # where 0 need to be masked
        # reversed_input_to_cudnn = [3, 2, 1, 0, 0]
        # output_from_cudnn = [6, 5, 4, 0, 0]
        # expected_output = [0, 0, 6, 5 ,4]
        inputs = array_ops.reverse_sequence_v2(
            inputs, sequence_lengths, seq_axis=seq_axis, batch_axis=batch_axis)
    outputs, h, c, _, _ = gen_cudnn_rnn_ops.CudnnRNNV3(
        input=inputs,
        input_h=init_h,
        input_c=init_c,
        params=params,
        is_training=True,
        rnn_mode='lstm',
        sequence_lengths=sequence_lengths,
        time_major=time_major)
    if go_backwards:
        outputs = array_ops.reverse_sequence_v2(
            outputs, sequence_lengths, seq_axis=seq_axis, batch_axis=batch_axis)
        outputs = array_ops.reverse(outputs, axis=[seq_axis])
else:
    # # Fill the array with shape [batch] with value of max timesteps.
    # sequence_length = array_ops.fill([array_ops.shape(inputs)[1]],
    #                                  array_ops.shape(inputs)[0])
    if go_backwards:
        # Reverse axis 0 since the input is already convert to time major.
        inputs = array_ops.reverse(inputs, axis=[0])
    outputs, h, c, _ = gen_cudnn_rnn_ops.CudnnRNN(
        input=inputs, input_h=init_h, input_c=init_c, params=params,
        is_training=True, rnn_mode='lstm')

last_output = outputs[-1]
if not time_major and mask is None:
    outputs = array_ops.transpose(outputs, perm=[1, 0, 2])
h = array_ops.squeeze(h, axis=seq_axis)
c = array_ops.squeeze(c, axis=seq_axis)

# In the case of variable length input, the cudnn kernel will fill zeros for
# the output, whereas the default keras behavior is to bring over the previous
# output for t-1, so that in the return_sequence=False case, user can quickly
# get the final effect output instead just 0s at the last timestep.
# In order to mimic the default keras behavior, we copy the final h state as
# the last_output, since it is numerically same as the output.
if mask is not None:
    last_output = h
exit((last_output, outputs, h, c, _runtime(_RUNTIME_GPU)))
