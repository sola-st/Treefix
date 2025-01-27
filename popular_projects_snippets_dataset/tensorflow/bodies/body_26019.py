# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/structured_function.py
nested_args = structure.from_compatible_tensor_list(
    self._input_structure, args)
if not _should_unpack(nested_args):
    nested_args = (nested_args,)
ret = self._func(*nested_args)
if _should_pack(ret):
    ret = tuple(ret)
ret = structure.to_tensor_list(self._output_structure, ret)
exit([ops.convert_to_tensor(t) for t in ret])
