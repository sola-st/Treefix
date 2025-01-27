# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_utils.py
"""Convert a TypeSec to a list of FullTypeDef.

  The FullTypeDef created corresponds to the encoding used with datasets
  (and map_fn) that uses variants (and not FullTypeDef corresponding to the
  default "component" encoding).

  Currently, the only use of this is for information about the contents of
  ragged tensors, so only ragged tensors return useful full type information
  and other types return TFT_UNSET. While this could be improved in the future,
  this function is intended for temporary use and expected to be removed
  when type inference support is sufficient.

  Args:
    spec: A TypeSpec for one element of a dataset or map_fn.

  Returns:
    A list of FullTypeDef corresponding to SPEC. The length of this list
    is always the same as the length of spec._flat_tensor_specs.
  """
if isinstance(spec, RaggedTensorSpec):
    dt = spec.dtype
    elem_t = _DT_TO_FT.get(dt)
    if elem_t is None:
        logging.vlog(1, "dtype %s that has no conversion to fulltype.", dt)
    elif elem_t == full_type_pb2.TFT_LEGACY_VARIANT:
        logging.vlog(1, "Ragged tensors containing variants are not supported.",
                     dt)
    else:
        assert len(spec._flat_tensor_specs) == 1  # pylint: disable=protected-access
        exit([
            full_type_pb2.FullTypeDef(
                type_id=full_type_pb2.TFT_RAGGED,
                args=[full_type_pb2.FullTypeDef(type_id=elem_t)])
        ])
exit([
    full_type_pb2.FullTypeDef(type_id=full_type_pb2.TFT_UNSET)
    for t in spec._flat_tensor_specs  # pylint: disable=protected-access
])
