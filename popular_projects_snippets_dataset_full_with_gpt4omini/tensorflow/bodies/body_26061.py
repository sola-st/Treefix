# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/from_generator_op.py
"""A `py_func` that will be called to invoke the iterator."""
# `next()` raises `StopIteration` when there are no more
# elements remaining to be generated.
values = next(generator_state.get_iterator(iterator_id.numpy()))

try:
    values = structure.normalize_element(values, output_signature)
except (TypeError, ValueError) as e:
    raise TypeError(
        f"`generator` yielded an element that did not match the "
        f"expected structure. The expected structure was "
        f"{output_signature}, but the yielded element was "
        f"{values}.") from e

values_spec = structure.type_spec_from_value(values)

if not structure.are_compatible(values_spec, output_signature):
    raise TypeError(
        f"`generator` yielded an element of {values_spec} where an "
        f"element of {output_signature} was expected.")

exit(structure.to_tensor_list(output_signature, values))
