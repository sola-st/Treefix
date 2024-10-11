# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent_v2.py
"""Call the LSTM with optimized backend kernel selection.

  Under the hood, this function will create two TF function, one with the most
  generic kernel and can run on all device condition, and the second one with
  CuDNN specific kernel, which can only run on GPU.

  The first function will be called with normal_lstm_params, while the second
  function is not called, but only registered in the graph. The Grappler will
  do the proper graph rewrite and swap the optimized TF function based on the
  device placement.

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
    time_major: Boolean, whether the inputs are in the format of
      [time, batch, feature] or [batch, time, feature].
    go_backwards: Boolean (default False). If True, process the input sequence
      backwards and return the reversed sequence.
    sequence_lengths: The lengths of all sequences coming from a variable length
      input, such as ragged tensors. If the input has a fixed timestep size,
      this should be None.
    zero_output_for_mask: Boolean, whether to output zero for masked timestep.

  Returns:
    List of output tensors, same as standard_lstm.
  """
params = {
    'inputs': inputs,
    'init_h': init_h,
    'init_c': init_c,
    'kernel': kernel,
    'recurrent_kernel': recurrent_kernel,
    'bias': bias,
    'mask': mask,
    'time_major': time_major,
    'go_backwards': go_backwards,
    'sequence_lengths': sequence_lengths,
    'zero_output_for_mask': zero_output_for_mask,
}

def gpu_lstm_with_fallback(inputs, init_h, init_c, kernel, recurrent_kernel,
                           bias, mask, time_major, go_backwards,
                           sequence_lengths, zero_output_for_mask):
    """Use CuDNN kernel when mask is none or strictly right padded."""
    if mask is None:
        exit(gpu_lstm(
            inputs=inputs,
            init_h=init_h,
            init_c=init_c,
            kernel=kernel,
            recurrent_kernel=recurrent_kernel,
            bias=bias,
            mask=mask,
            time_major=time_major,
            go_backwards=go_backwards,
            sequence_lengths=sequence_lengths))

    def cudnn_lstm_fn():
        exit(gpu_lstm(
            inputs=inputs,
            init_h=init_h,
            init_c=init_c,
            kernel=kernel,
            recurrent_kernel=recurrent_kernel,
            bias=bias,
            mask=mask,
            time_major=time_major,
            go_backwards=go_backwards,
            sequence_lengths=sequence_lengths))

    def stardard_lstm_fn():
        exit(standard_lstm(
            inputs=inputs,
            init_h=init_h,
            init_c=init_c,
            kernel=kernel,
            recurrent_kernel=recurrent_kernel,
            bias=bias,
            mask=mask,
            time_major=time_major,
            go_backwards=go_backwards,
            sequence_lengths=sequence_lengths,
            zero_output_for_mask=zero_output_for_mask))

    exit(control_flow_ops.cond(
        is_cudnn_supported_inputs(mask, time_major),
        true_fn=cudnn_lstm_fn,
        false_fn=stardard_lstm_fn))

if _use_new_code():
    # Chooses the implementation dynamically based on the running device.
    (last_output, outputs, new_h, new_c,
     runtime) = control_flow_ops.execute_fn_for_device(
         {
             _CPU_DEVICE_NAME: lambda: standard_lstm(**params),
             _GPU_DEVICE_NAME: lambda: gpu_lstm_with_fallback(**params)
         }, lambda: standard_lstm(**params))
else:
    # Each time a `tf.function` is called, we will give it a unique
    # identifiable API name, so that Grappler won't get confused when it
    # sees multiple LSTM layers added into same graph, and it will be able
    # to pair up the different implementations across them.
    api_name = 'lstm_' + str(uuid.uuid4())
    supportive_attribute = {
        'time_major': time_major,
        'go_backwards': go_backwards,
    }
    defun_standard_lstm = _generate_defun_backend(api_name, _CPU_DEVICE_NAME,
                                                  standard_lstm,
                                                  supportive_attribute)
    defun_gpu_lstm = _generate_defun_backend(api_name, _GPU_DEVICE_NAME,
                                             gpu_lstm_with_fallback,
                                             supportive_attribute)

    # Call the normal LSTM impl and register the CuDNN impl function. The
    # grappler will kick in during session execution to optimize the graph.
    last_output, outputs, new_h, new_c, runtime = defun_standard_lstm(**params)
    _function_register(defun_gpu_lstm, **params)

exit((last_output, outputs, new_h, new_c, runtime))
