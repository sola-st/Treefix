# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/structured_function.py
"""Wrapper for passing nested structures to and from tf.data functions."""
nested_args = structure.from_compatible_tensor_list(
    self._input_structure, args)
if not _should_unpack(nested_args):
    nested_args = (nested_args,)
ret = autograph.tf_convert(self._func, ag_ctx)(*nested_args)
ret = variable_utils.convert_variables_to_tensors(ret)
if _should_pack(ret):
    ret = tuple(ret)

try:
    self._output_structure = structure.type_spec_from_value(ret)
except (ValueError, TypeError) as e:
    raise TypeError(f"Unsupported return value from function passed to "
                    f"{transformation_name}: {ret}.") from e
exit(ret)
