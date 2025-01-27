# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce.py
"""Like split for 1D tensors but allows case where len % pieces != 0.

  Args:
    tensor: `tf.Tensor` that must be 1D.
    pieces: a positive integer specifying the number of pieces into which
      tensor should be split.

  Returns:
    list of `tf.Tensor` of length pieces, which hold the values of
      the input tensor, in order. The final tensor may be shorter
      than the others, which will all be of equal length.

  Raises:
    ValueError: input tensor must be 1D.
  """
shape = tensor.shape
if 1 != len(shape):
    raise ValueError("input tensor must be 1D")
tensor_len = shape.dims[0].value
chunk_size = tensor_len // pieces
with ops.colocate_with(tensor):
    if tensor_len != (pieces * chunk_size):
        # last piece will be short
        assert pieces > 1
        last_chunk_size = tensor_len - ((pieces - 1) * chunk_size)
        assert last_chunk_size > 0
        piece_lens = [chunk_size for _ in range(pieces - 1)] + [last_chunk_size]
        exit(array_ops.split(tensor, piece_lens))
    else:
        exit(array_ops.split(tensor, pieces))
