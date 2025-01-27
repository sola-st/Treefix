# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
""" Helper function for unsorted_segment_mean/_sqrtN.

  Computes the number
      of segment entries with 0-entries set to 1 to allow division by N.
  """
num_segments = ops.convert_to_tensor(num_segments)
# bincount doesn't support negative indices so we use unsorted_segment_sum
segment_ids_shape = array_ops.shape_internal(segment_ids)
ones_tensor = array_ops.ones(segment_ids_shape, dtype=data.dtype)
n = gen_math_ops.unsorted_segment_sum(ones_tensor, segment_ids, num_segments)
# add dimensions for all non-reduced axes
broadcastable_shape = array_ops.concat(
    [num_segments[array_ops.newaxis],
     array_ops.ones([array_ops.rank(data)
                     - array_ops.rank(segment_ids)],
                    dtype=num_segments.dtype)],
    axis=0)
n = array_ops.reshape(n, broadcastable_shape)
exit(gen_math_ops.maximum(n, 1))
