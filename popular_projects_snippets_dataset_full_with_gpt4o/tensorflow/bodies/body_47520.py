# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent_v2.py
"""GRU with CuDNN implementation which is only available for GPU."""
if not time_major and mask is None:
    inputs = array_ops.transpose(inputs, perm=(1, 0, 2))
    seq_axis, batch_axis = (0, 1)
else:
    seq_axis, batch_axis = (0, 1) if time_major else (1, 0)
# For init_h, cuDNN expects one more dim of num_layers before or after batch
# dim for time major or batch major inputs respectively
init_h = array_ops.expand_dims(init_h, axis=seq_axis)

weights = array_ops.split(kernel, 3, axis=1)
weights += array_ops.split(recurrent_kernel, 3, axis=1)
# Note that the bias was initialized as shape (2, 3 * units), flat it into
# (6 * units)
bias = array_ops.split(backend.flatten(bias), 6)

if sysconfig.get_build_info()['is_cuda_build']:
    # Note that the gate order for CuDNN is different from the canonical format.
    # canonical format is [z, r, h], whereas CuDNN is [r, z, h]. The swap need
    # to be done for kernel, recurrent_kernel, input_bias, recurrent_bias.
    # z is update gate weights.
    # r is reset gate weights.
    # h is output gate weights.
    weights[0], weights[1] = weights[1], weights[0]
    weights[3], weights[4] = weights[4], weights[3]
    bias[0], bias[1] = bias[1], bias[0]
    bias[3], bias[4] = bias[4], bias[3]

params = _canonical_to_params(
    weights=weights,
    biases=bias,
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
    outputs, h, _, _, _ = gen_cudnn_rnn_ops.CudnnRNNV3(
        input=inputs,
        input_h=init_h,
        input_c=0,
        params=params,
        is_training=True,
        rnn_mode='gru',
        sequence_lengths=sequence_lengths,
        time_major=time_major)
    if go_backwards:
        outputs = array_ops.reverse_sequence_v2(
            outputs, sequence_lengths, seq_axis=seq_axis, batch_axis=batch_axis)
        outputs = array_ops.reverse(outputs, axis=[seq_axis])
else:
    if go_backwards:
        # Reverse axis 0 since the input is already convert to time major.
        inputs = array_ops.reverse(inputs, axis=[0])
    outputs, h, _, _ = gen_cudnn_rnn_ops.CudnnRNN(
        input=inputs, input_h=init_h, input_c=0, params=params,
        is_training=True, rnn_mode='gru')

last_output = outputs[-1]
if not time_major and mask is None:
    outputs = array_ops.transpose(outputs, perm=[1, 0, 2])
h = array_ops.squeeze(h, axis=seq_axis)

# In the case of variable length input, the cudnn kernel will fill zeros for
# the output, whereas the default keras behavior is to bring over the previous
# output for t-1, so that in the return_sequence=False case, user can quickly
# get the final effect output instead just 0s at the last timestep.
# In order to mimic the default keras behavior, we copy the final h state as
# the last_output, since it is numerically same as the output.
if mask is not None:
    last_output = h

exit((last_output, outputs, h, _runtime(_RUNTIME_GPU)))
