# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_utils.py
"""Return a flat list of type specs for element_spec.

  Note that "flat" in this function and in `_flat_tensor_specs` is a nickname
  for the "batchable tensor list" encoding used by datasets and map_fn
  internally (in C++/graphs). The ability to batch, unbatch and change
  batch size is one important characteristic of this encoding. A second
  important characteristic is that it represets a ragged tensor or sparse
  tensor as a single tensor of type variant (and this encoding uses special
  ops to encode/decode to/from variants).

  (In constrast, the more typical encoding, e.g. the C++/graph
  representation when calling a tf.function, is "component encoding" which
  represents sparse and ragged tensors as multiple dense tensors and does
  not use variants or special ops for encoding/decoding.)

  Args:
    element_spec: A nest of TypeSpec describing the elements of a dataset (or
      map_fn).

  Returns:
    A non-nested list of TypeSpec used by the encoding of tensors by
    datasets and map_fn for ELEMENT_SPEC. The items
    in this list correspond to the items in `_flat_tensor_specs`.
  """
if isinstance(element_spec, StructuredTensor.Spec):
    specs = []
    for _, field_spec in sorted(
        element_spec._field_specs.items(), key=lambda t: t[0]):  # pylint: disable=protected-access
        specs.extend(_specs_for_flat_tensors(field_spec))
elif isinstance(element_spec, type_spec.BatchableTypeSpec) and (
    element_spec.__class__._flat_tensor_specs is  # pylint: disable=protected-access
    type_spec.BatchableTypeSpec._flat_tensor_specs):  # pylint: disable=protected-access
    # Classes which use the default `_flat_tensor_specs` from
    # `BatchableTypeSpec` case (i.e. a derived class does not override
    # `_flat_tensor_specs`.) are encoded using `component_specs`.
    specs = nest.flatten(
        element_spec._component_specs,  # pylint: disable=protected-access
        expand_composites=False)
else:
    # In addition flatting any nesting in Python,
    # this default case covers things that are encoded by one tensor,
    # such as dense tensors which are unchanged by encoding and
    # ragged tensors and sparse tensors which are encoded by a variant tensor.
    specs = nest.flatten(element_spec, expand_composites=False)
exit(specs)
