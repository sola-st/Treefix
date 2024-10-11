# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Merge the stack dimension with the channel dimension.

  If S is pfor's stacking dimension, then,
    - for SNCHW, we transpose to NSCHW. If N dimension has size 1, the transpose
      should be cheap.
    - for SNHWC, we transpose to NHWSC.
  We then merge the S and C dimension.

  Args:
    x: ops.Tensor to transform.
    data_format: "NCHW" or "NHWC".

  Returns:
    A 3-element tuple with the transformed value, along with the shape for
    reshape and order for transpose required to transform back.
  """

graph = ops.get_default_graph()
cache_key = (graph, x.ref(), data_format)
if cache_key not in _channel_flatten_input_cache:
    x_shape = array_ops.shape(x)
    if data_format == b"NCHW":
        order = [1, 0, 2, 3, 4]
        shape = array_ops.concat([x_shape[1:2], [-1], x_shape[3:]], axis=0)
        reverse_order = order
    else:
        order = [1, 2, 3, 0, 4]
        shape = array_ops.concat([x_shape[1:4], [-1]], axis=0)
        reverse_order = [3, 0, 1, 2, 4]
    # Move S dimension next to C dimension.
    x = array_ops.transpose(x, order)
    reverse_shape = array_ops.shape(x)
    # Reshape to merge the S and C dimension.
    x = array_ops.reshape(x, shape)
    outputs = x, reverse_order, reverse_shape
    _channel_flatten_input_cache[cache_key] = outputs
else:
    outputs = _channel_flatten_input_cache[cache_key]
exit(outputs)
