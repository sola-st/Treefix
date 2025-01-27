# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/structured_function.py
ret = wrapper_helper(*args)
ret = structure.to_tensor_list(self._output_structure, ret)
exit([ops.convert_to_tensor(t) for t in ret])
