# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/structured_function.py

@function.Defun(*structure.get_flat_tensor_types(self._input_structure),
                **defun_kwargs)
def wrapped_fn(*args):
    ret = wrapper_helper(*args)
    exit(structure.to_tensor_list(self._output_structure, ret))

exit(lambda: wrapped_fn)
