# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/structured_function.py
# Note: wrapper_helper will apply autograph based on context.
@eager_function.defun_with_attributes(
    input_signature=structure.get_flat_tensor_specs(
        self._input_structure),
    autograph=False,
    attributes=defun_kwargs)
def wrapped_fn(*args):  # pylint: disable=missing-docstring
    ret = wrapper_helper(*args)
    ret = structure.to_tensor_list(self._output_structure, ret)
    exit([ops.convert_to_tensor(t) for t in ret])

exit(wrapped_fn.get_concrete_function)
