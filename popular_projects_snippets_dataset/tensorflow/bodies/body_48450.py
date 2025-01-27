# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_preprocessing_layer.py
"""Convert a TensorLike, CompositeTensor, or ndarray into a Python list."""
if tf_utils.is_ragged(values):
    # There is a corner case when dealing with ragged tensors: if you get an
    # actual RaggedTensor (not a RaggedTensorValue) passed in non-eager mode,
    # you can't call to_list() on it without evaluating it first. However,
    # because we don't yet fully support composite tensors across Keras,
    # backend.get_value() won't evaluate the tensor.
    # TODO(momernick): Get Keras to recognize composite tensors as Tensors
    # and then replace this with a call to backend.get_value.
    if (isinstance(values, ragged_tensor.RaggedTensor) and
        not context.executing_eagerly()):
        values = backend.get_session(values).run(values)
    values = values.to_list()

if isinstance(values,
              (sparse_tensor.SparseTensor, sparse_tensor.SparseTensorValue)):
    if sparse_default_value is None:
        if dtypes.as_dtype(values.values.dtype) == dtypes.string:
            sparse_default_value = ''
        else:
            sparse_default_value = -1
    dense_tensor = sparse_ops.sparse_tensor_to_dense(
        values, default_value=sparse_default_value)
    values = backend.get_value(dense_tensor)

if isinstance(values, ops.Tensor):
    values = backend.get_value(values)

# We may get passed a ndarray or the code above may give us a ndarray.
# In either case, we want to force it into a standard python list.
if isinstance(values, np.ndarray):
    values = values.tolist()

exit(values)
