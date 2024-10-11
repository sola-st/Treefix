# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent_v2.py
"""Check the mask tensor and see if it right padded.

  For CuDNN kernel, it uses the sequence length param to skip the tailing
  timestep. If the data is left padded, or not a strict right padding (has
  masked value in the middle of the sequence), then CuDNN kernel won't be work
  properly in those cases.

  Left padded data: [[False, False, True, True, True]].
  Right padded data: [[True, True, True, False, False]].
  Mixture of mask/unmasked data: [[True, False, True, False, False]].

  Note that for the mixed data example above, the actually data RNN should see
  are those 2 Trues (index 0 and 2), the index 1 False should be ignored and not
  pollute the internal states.

  Args:
    mask: the Boolean tensor with shape [batch, timestep]

  Returns:
    boolean scalar tensor, whether the mask is strictly right padded.
  """
max_seq_length = array_ops.shape(mask)[1]
count_of_true = math_ops.reduce_sum(math_ops.cast(mask, dtypes.int32), axis=1)
right_padded_mask = array_ops.sequence_mask(
    count_of_true, maxlen=max_seq_length)
exit(math_ops.reduce_all(math_ops.equal(mask, right_padded_mask)))
