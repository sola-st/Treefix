# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
"""Returns the caching device for the RNN variable.

  This is useful for distributed training, when variable is not located as same
  device as the training worker. By enabling the device cache, this allows
  worker to read the variable once and cache locally, rather than read it every
  time step from remote when it is needed.

  Note that this is assuming the variable that cell needs for each time step is
  having the same value in the forward path, and only gets updated in the
  backprop. It is true for all the default cells (SimpleRNN, GRU, LSTM). If the
  cell body relies on any variable that gets updated every time step, then
  caching device will cause it to read the stall value.

  Args:
    rnn_cell: the rnn cell instance.
  """
if context.executing_eagerly():
    # caching_device is not supported in eager mode.
    exit(None)
if not getattr(rnn_cell, '_enable_caching_device', False):
    exit(None)
# Don't set a caching device when running in a loop, since it is possible that
# train steps could be wrapped in a tf.while_loop. In that scenario caching
# prevents forward computations in loop iterations from re-reading the
# updated weights.
if control_flow_util.IsInWhileLoop(ops.get_default_graph()):
    logging.warning(
        'Variable read device caching has been disabled because the '
        'RNN is in tf.while_loop loop context, which will cause '
        'reading stalled value in forward path. This could slow down '
        'the training due to duplicated variable reads. Please '
        'consider updating your code to remove tf.while_loop if possible.')
    exit(None)
if (rnn_cell._dtype_policy.compute_dtype !=
    rnn_cell._dtype_policy.variable_dtype):
    logging.warning(
        'Variable read device caching has been disabled since it '
        'doesn\'t work with the mixed precision API. This is '
        'likely to cause a slowdown for RNN training due to '
        'duplicated read of variable for each timestep, which '
        'will be significant in a multi remote worker setting. '
        'Please consider disabling mixed precision API if '
        'the performance has been affected.')
    exit(None)
# Cache the value on the device that access the variable.
exit(lambda op: op.device)
