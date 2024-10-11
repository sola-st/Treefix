# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Register the `cls` as supported value type of RaggedTenosr.

  The cls must be a subclass of CompositeTensor, and must support:
   - Spec:
     The Spec must be a `BatchableTypeSpec`
   - Properties:
     - x.shape
     - x.dtype
   - Methods:
     - x.__getitem__(idx) (method: returns a supported value type)
     - x.set_shape(shape)
   - Ops:
     - tf.shape(x) -- tf.shape(x)[0] must be a tf.Tensor.
     - tf.tile(x)
     - assert_rank_at_least(x)
     - tf.ones_like(x)
     - tf.gather(params=x, indices=Tensor)
     - tf.add(x, y)
     - tf.boolean_mask(x, ...)
     - @TODO(edloper): Complete this list

   Note: the following RaggedTensor, RaggedTensorSpec methods & ops are not
   currently supported unless `rt.values` is a RaggedTensor or a tf.Tensor:
     - rt.to_tensor()
     - rt.to_sparse_tensor()
     - rt._to_variant()
     - rt._from_variant()
     - tf.ragged.cross([rt])
     - tf.gather(params=x, indices=rt)  # rt used for indices
     - RaggedTensorSpec methods:
       - _batch
       - _unbatch
       - _to_tensor_list
       - _to_batched_tensor_list
       - _from_compatible_tensor_list

  Args:
    cls: The type to be added to supported value types.
  """
if not issubclass(cls, composite_tensor.CompositeTensor):
    raise ValueError(f"cls ({cls}) must be a subclass of CompositeTensor.")
if not hasattr(cls, "shape"):
    raise ValueError("cls must support the `shape` property.")
if not hasattr(cls, "dtype"):
    raise ValueError("cls must support the `dtype` property.")
global _SUPPORTED_RAGGED_VALUE_TYPES
_SUPPORTED_RAGGED_VALUE_TYPES += (cls,)
