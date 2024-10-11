# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Decodes the output of a softmax.

  Can use either greedy search (also known as best path)
  or a constrained dictionary search.

  Args:
      y_pred: tensor `(samples, time_steps, num_categories)`
          containing the prediction, or output of the softmax.
      input_length: tensor `(samples, )` containing the sequence length for
          each batch item in `y_pred`.
      greedy: perform much faster best-path search if `true`.
          This does not use a dictionary.
      beam_width: if `greedy` is `false`: a beam search decoder will be used
          with a beam of this width.
      top_paths: if `greedy` is `false`,
          how many of the most probable paths will be returned.

  Returns:
      Tuple:
          List: if `greedy` is `true`, returns a list of one element that
              contains the decoded sequence.
              If `false`, returns the `top_paths` most probable
              decoded sequences.
              Each decoded sequence has shape (samples, time_steps).
              Important: blank labels are returned as `-1`.
          Tensor `(top_paths, )` that contains
              the log probability of each decoded sequence.
  """
input_shape = shape(y_pred)
num_samples, num_steps = input_shape[0], input_shape[1]
y_pred = math_ops.log(array_ops.transpose(y_pred, perm=[1, 0, 2]) + epsilon())
input_length = math_ops.cast(input_length, dtypes_module.int32)

if greedy:
    (decoded, log_prob) = ctc.ctc_greedy_decoder(
        inputs=y_pred, sequence_length=input_length)
else:
    (decoded, log_prob) = ctc.ctc_beam_search_decoder(
        inputs=y_pred,
        sequence_length=input_length,
        beam_width=beam_width,
        top_paths=top_paths)
decoded_dense = []
for st in decoded:
    st = sparse_tensor.SparseTensor(
        st.indices, st.values, (num_samples, num_steps))
    decoded_dense.append(
        sparse_ops.sparse_tensor_to_dense(sp_input=st, default_value=-1))
exit((decoded_dense, log_prob))
