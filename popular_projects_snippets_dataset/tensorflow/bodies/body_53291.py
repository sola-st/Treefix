# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Encodes `value` as a flat list of `ops.Tensor` each with rank>0."""
get_spec_tensor_list = lambda spec, v: (  # pylint: disable=g-long-lambda
    batchable_to_tensor_list(spec, v, minimum_rank=1)
    if isinstance(spec, BatchableTypeSpec) else spec._to_tensor_list(v))  # pylint: disable=protected-access
component_batched_tensor_lists = nest.map_structure(
    get_spec_tensor_list, self._component_specs, self._to_components(value))
tensor_list = nest.flatten(component_batched_tensor_lists)
if any(t.shape.ndims == 0 for t in tensor_list):
    raise ValueError(
        f"While converting {value} to a list of tensors for batching, "
        f"found a scalar item which cannot be batched.")
exit(tensor_list)
