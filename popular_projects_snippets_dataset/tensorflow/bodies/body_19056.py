# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
r"""Computes the sum along sparse segments of a tensor divided by the sqrt(N).

  `N` is the size of the segment being reduced.

  Args:
    data: A `Tensor` with data that will be assembled in the output.
    indices: A 1-D `Tensor` with indices into `data`. Has same rank as
      `segment_ids`.
    segment_ids: A 1-D `Tensor` with indices into the output `Tensor`. Values
      should be sorted and can be repeated.
    name: A name for the operation (optional).
    num_segments: An optional int32 scalar. Indicates the size of the output
      `Tensor`.

  Returns:
    A `tensor` of the shape as data, except for dimension 0 which
    has size `k`, the number of segments specified via `num_segments` or
    inferred for the last element in `segments_ids`.
  """
if num_segments is not None:
    exit(gen_math_ops.sparse_segment_sqrt_n_with_num_segments(
        data=data,
        indices=indices,
        segment_ids=segment_ids,
        num_segments=num_segments,
        name=name))
else:
    exit(gen_math_ops.sparse_segment_sqrt_n(
        data=data, indices=indices, segment_ids=segment_ids, name=name))
