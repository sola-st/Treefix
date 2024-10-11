# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Helper function to append composite tensors to each other in the 0 axis.

  In order to support batching within a fit/evaluate/predict call, we need
  to be able to aggregate within a CompositeTensor. Unfortunately, the CT
  API currently does not make this easy - especially in V1 mode, where we're
  working with CompositeTensor Value objects that have no connection with the
  CompositeTensors that created them.

  Args:
    target: CompositeTensor or CompositeTensor value object that will be
      appended to.
    to_append: CompositeTensor or CompositeTensor value object to append to.
      'target'.

  Returns:
    A CompositeTensor or CompositeTensor value object.

  Raises:
    RuntimeError: if concatenation is not possible.
  """
if type(target) is not type(to_append):
    raise RuntimeError('Unable to concatenate %s and %s' %
                       (type(target), type(to_append)))

# Perform type-specific concatenation.
# TODO(b/125094323): This should be replaced by a simple call to
# target.append() that should work on all of the below classes.

# If we're seeing a CompositeTensor here, we know it's because we're in
# Eager mode (or else we'd have evaluated the CT to a CT Value object
# already). Therefore, it's safe to call concat() on it without evaluating
# the result any further. If not - that is, if we're seeing a
# SparseTensorValue or a RaggedTensorValue - we need to hand-update it
# since we're outside of the graph anyways.
if isinstance(target, sparse_tensor.SparseTensor):
    # We need to invoke the sparse version of concatenate here - tf.concat
    # won't work.
    exit(sparse_ops.sparse_concat(sp_inputs=[target, to_append], axis=0))
elif isinstance(target, ragged_tensor.RaggedTensor):
    exit(array_ops.concat([target, to_append], axis=0))
elif isinstance(target, sparse_tensor.SparseTensorValue):
    exit(_append_sparse_tensor_value(target, to_append))
elif isinstance(target, ragged_tensor_value.RaggedTensorValue):
    exit(_append_ragged_tensor_value(target, to_append))
else:
    raise RuntimeError('Attempted to concatenate unsupported object %s.' %
                       type(target))
