# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
# Prepend a 1 for the batch dimension; for recurrent
# variational dropout we use the same dropout mask for all
# batch elements.
exit(array_ops.concat(([1], tensor_shape.TensorShape(s).as_list()), 0))
