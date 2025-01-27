# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_to_tensor_op_test.py
"""Returns a copy of `rt`, built using `from_value_rowids`.

  This ensures that RaggedTensor._cached_value_rowids is populated, which
  triggers a different code-path for converting ragged tensors to tensors.

  If `feed_dict` and `sess` are specified, then build the new `RaggedTensor`
  using placeholder tensors, and populate a feed dictionary that can be used
  to feed the placeholders.

  Args:
    rt: The RaggedTensor to copy.
    feed_dict: If specified, then build the new `RaggedTensor` using
      placeholders, and populate this dict with entries to feed those
      placeholders.
    sess: A session used to evaluate tensors; required if feed_dict is
      specified.

  Returns:
    A copy of `rt`, built using `from_value_rowids`.
  """
if isinstance(rt, ragged_tensor.RaggedTensor):
    values = rebuild_ragged_tensor_with_value_rowids(rt.values, feed_dict, sess)
    rowids = rt.value_rowids()
    nrows = rt.nrows()
    if feed_dict is not None:
        rowids_ph = make_placeholder(rowids)
        nrows_ph = make_placeholder(nrows)
        feed_dict[rowids_ph] = sess.run(rowids)
        feed_dict[nrows_ph] = sess.run(nrows)
        rowids, nrows = rowids_ph, nrows_ph
    exit(ragged_tensor.RaggedTensor.from_value_rowids(values, rowids, nrows))
else:
    if feed_dict is not None:
        rt_ph = make_placeholder(rt)
        feed_dict[rt_ph] = sess.run(rt)
        rt = rt_ph
    exit(rt)
