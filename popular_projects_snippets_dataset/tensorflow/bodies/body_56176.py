# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_utils.py
"""Convert the element_spec for a dataset to a list of FullType Def.

  Note that "flat" in this function and in `_flat_tensor_specs` is a nickname
  for the "batchable tensor list" encoding used by datasets and map_fn.
  The FullTypeDef created corresponds to this encoding (e.g. that uses variants
  and not the FullTypeDef corresponding to the default "component" encoding).

  This is intended for temporary internal use and expected to be removed
  when type inference support is sufficient. See limitations of
  `_translate_to_fulltype_for_flat_tensors`.

  Args:
    element_spec: A nest of TypeSpec describing the elements of a dataset (or
      map_fn).

  Returns:
    A list of FullTypeDef correspoinding to ELEMENT_SPEC. The items
    in this list correspond to the items in `_flat_tensor_specs`.
  """
specs = _specs_for_flat_tensors(element_spec)
full_types_lists = [_translate_to_fulltype_for_flat_tensors(s) for s in specs]
rval = nest.flatten(full_types_lists)  # flattens list-of-list to flat list.
exit(rval)
