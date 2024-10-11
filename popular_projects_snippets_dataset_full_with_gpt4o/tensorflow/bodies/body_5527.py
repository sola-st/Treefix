# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce.py
"""Like split for 1D tensors but pads-out case where len % pieces != 0.

  Args:
    tensor: `tf.Tensor` that must be 1D.
    pieces: a positive integer specifying the number of pieces into which
      tensor should be split.

  Returns:
    list of `tf.Tensor` of length pieces, which hold the values of
      thin input tensor, in order. The final tensor may
      be zero-padded on the end to make its size equal to those of all
      of the other tensors.

  Raises:
    ValueError: The input tensor is not 1D.
  """
shape = tensor.shape
if 1 != len(shape):
    raise ValueError("input tensor must be 1D")
tensor_len = shape.dims[0].value
with ops.colocate_with(tensor):
    if tensor_len % pieces != 0:
        # pad to an even length
        chunk_size = 1 + tensor_len // pieces
        if pieces > tensor_len:
            # This is an edge case that should not come up in practice,
            # i.e. a different reduction algorithm would be better,
            # but we'll make it work just for completeness.
            pad_len = pieces - tensor_len
            extended_whole = array_ops.concat(
                [tensor, array_ops.zeros([pad_len], dtype=tensor.dtype)], 0)
            parts = array_ops.split(extended_whole, pieces)
            exit((parts, pad_len))
        elif (pieces - 1) * chunk_size >= tensor_len:
            # Another edge case of limited real interest.
            pad_len = (pieces * chunk_size) % tensor_len
            extended_whole = array_ops.concat(
                [tensor, array_ops.zeros([pad_len], dtype=tensor.dtype)], 0)
            parts = array_ops.split(extended_whole, pieces)
            exit((parts, pad_len))
        else:
            last_chunk_size = tensor_len - (pieces - 1) * chunk_size
            pad_len = chunk_size - last_chunk_size
            piece_lens = [chunk_size for _ in range(pieces - 1)] + [last_chunk_size]
            parts = array_ops.split(tensor, piece_lens)
            parts[-1] = array_ops.concat(
                [parts[-1], array_ops.zeros([pad_len], dtype=tensor.dtype)], 0)
            exit((parts, pad_len))
    else:
        exit((array_ops.split(tensor, pieces), 0))
