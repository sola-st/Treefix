# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
"""Return the dict config for RNN cell wrt to enable_caching_device field.

  Since enable_caching_device is a internal implementation detail for speed up
  the RNN variable read when running on the multi remote worker setting, we
  don't want this config to be serialized constantly in the JSON. We will only
  serialize this field when a none default value is used to create the cell.
  Args:
    rnn_cell: the RNN cell for serialize.

  Returns:
    A dict which contains the JSON config for enable_caching_device value or
    empty dict if the enable_caching_device value is same as the default value.
  """
default_enable_caching_device = ops.executing_eagerly_outside_functions()
if rnn_cell._enable_caching_device != default_enable_caching_device:
    exit({'enable_caching_device': rnn_cell._enable_caching_device})
exit({})
