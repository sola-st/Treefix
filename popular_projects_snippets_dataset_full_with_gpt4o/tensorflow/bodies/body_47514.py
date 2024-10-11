# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent_v2.py
# return_runtime is a flag for testing, which shows the real backend
# implementation chosen by grappler in graph mode.
self._return_runtime = kwargs.pop('return_runtime', False)

super(GRU, self).__init__(
    units,
    activation=activation,
    recurrent_activation=recurrent_activation,
    use_bias=use_bias,
    kernel_initializer=kernel_initializer,
    recurrent_initializer=recurrent_initializer,
    bias_initializer=bias_initializer,
    kernel_regularizer=kernel_regularizer,
    recurrent_regularizer=recurrent_regularizer,
    bias_regularizer=bias_regularizer,
    activity_regularizer=activity_regularizer,
    kernel_constraint=kernel_constraint,
    recurrent_constraint=recurrent_constraint,
    bias_constraint=bias_constraint,
    dropout=dropout,
    recurrent_dropout=recurrent_dropout,
    implementation=kwargs.pop('implementation', 2),
    return_sequences=return_sequences,
    return_state=return_state,
    go_backwards=go_backwards,
    stateful=stateful,
    unroll=unroll,
    time_major=time_major,
    reset_after=reset_after,
    **kwargs)
# GPU kernel uses following setting by default and not configurable.
self._could_use_gpu_kernel = (
    self.activation in (activations.tanh, nn.tanh) and
    self.recurrent_activation in (activations.sigmoid, nn.sigmoid) and
    recurrent_dropout == 0 and not unroll and use_bias and
    reset_after and ops.executing_eagerly_outside_functions())
if config.list_logical_devices('GPU'):
    # Only show the message when there is GPU available, user will not care
    # about the cuDNN if there isn't any GPU.
    if self._could_use_gpu_kernel:
        logging.debug(_CUDNN_AVAILABLE_MSG % self.name)
    else:
        logging.warning(_CUDNN_NOT_AVAILABLE_MSG % self.name)

if _use_new_code():
    self._defun_wrapper = _DefunWrapper(time_major, go_backwards, 'gru')
