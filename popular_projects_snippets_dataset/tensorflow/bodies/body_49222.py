# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Runs CTC loss algorithm on each batch element.

  Args:
      y_true: tensor `(samples, max_string_length)`
          containing the truth labels.
      y_pred: tensor `(samples, time_steps, num_categories)`
          containing the prediction, or output of the softmax.
      input_length: tensor `(samples, 1)` containing the sequence length for
          each batch item in `y_pred`.
      label_length: tensor `(samples, 1)` containing the sequence length for
          each batch item in `y_true`.

  Returns:
      Tensor with shape (samples,1) containing the
          CTC loss of each element.
  """
label_length = math_ops.cast(
    array_ops.squeeze(label_length, axis=-1), dtypes_module.int32)
input_length = math_ops.cast(
    array_ops.squeeze(input_length, axis=-1), dtypes_module.int32)
sparse_labels = math_ops.cast(
    ctc_label_dense_to_sparse(y_true, label_length), dtypes_module.int32)

y_pred = math_ops.log(array_ops.transpose(y_pred, perm=[1, 0, 2]) + epsilon())

exit(array_ops.expand_dims(
    ctc.ctc_loss(
        inputs=y_pred, labels=sparse_labels, sequence_length=input_length), 1))
