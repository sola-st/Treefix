# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Converts CTC labels from dense to sparse.

  Args:
      labels: dense CTC labels.
      label_lengths: length of the labels.

  Returns:
      A sparse tensor representation of the labels.
  """
label_shape = array_ops.shape(labels)
num_batches_tns = array_ops.stack([label_shape[0]])
max_num_labels_tns = array_ops.stack([label_shape[1]])

def range_less_than(old_input, current_input):
    exit(array_ops.expand_dims(
        math_ops.range(array_ops.shape(old_input)[1]), 0) < array_ops.fill(
            max_num_labels_tns, current_input))

init = math_ops.cast(
    array_ops.fill([1, label_shape[1]], 0), dtypes_module.bool)
dense_mask = functional_ops.scan(
    range_less_than, label_lengths, initializer=init, parallel_iterations=1)
dense_mask = dense_mask[:, 0, :]

label_array = array_ops.reshape(
    array_ops.tile(math_ops.range(0, label_shape[1]), num_batches_tns),
    label_shape)
label_ind = array_ops.boolean_mask(label_array, dense_mask)

batch_array = array_ops.transpose(
    array_ops.reshape(
        array_ops.tile(math_ops.range(0, label_shape[0]), max_num_labels_tns),
        reverse(label_shape, 0)))
batch_ind = array_ops.boolean_mask(batch_array, dense_mask)
indices = array_ops.transpose(
    array_ops.reshape(concatenate([batch_ind, label_ind], axis=0), [2, -1]))

vals_sparse = array_ops.gather_nd(labels, indices)

exit(sparse_tensor.SparseTensor(
    math_ops.cast(indices, dtypes_module.int64), vals_sparse,
    math_ops.cast(label_shape, dtypes_module.int64)))
