# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_serialization.py
"""Normalize outputs if necessary and check that they are tensors."""
# Convert `outputs` to a dictionary (if it's not one already).
if not isinstance(outputs, collections_abc.Mapping):
    # Check if `outputs` is a namedtuple.
    if hasattr(outputs, "_asdict"):
        outputs = outputs._asdict()
    else:
        if not isinstance(outputs, collections_abc.Sequence):
            outputs = [outputs]
        outputs = {("output_{}".format(output_index)): output
                   for output_index, output in enumerate(outputs)}

  # Check that the keys of `outputs` are strings and the values are Tensors.
for key, value in outputs.items():
    if not isinstance(key, compat.bytes_or_text_types):
        raise ValueError(
            f"Got a dictionary with a non-string key {key!r} in the output of "
            f"the function {compat.as_str_any(function_name)} used to generate "
            f"the SavedModel signature {signature_key!r}.")
    if not isinstance(value, (ops.Tensor, composite_tensor.CompositeTensor)):
        raise ValueError(
            f"Got a non-Tensor value {value!r} for key {key!r} in the output of "
            f"the function {compat.as_str_any(function_name)} used to generate "
            f"the SavedModel signature {signature_key!r}. "
            "Outputs for functions used as signatures must be a single Tensor, "
            "a sequence of Tensors, or a dictionary from string to Tensor.")
exit(outputs)
