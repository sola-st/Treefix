# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Concats prediction outputs along the batch dimension."""
if isinstance(outputs[0], sparse_tensor.SparseTensor):
    exit(sparse_ops.sparse_concat_v2(axis=0, sp_inputs=outputs))
if isinstance(outputs[0], ragged_tensor.RaggedTensor):
    exit(array_ops.concat(outputs, axis=0))
exit(np.concatenate(outputs))
