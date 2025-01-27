# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/structured_function.py
# First we trace the function to infer the output structure.
@eager_function.defun_with_attributes(
    input_signature=structure.get_flat_tensor_specs(
        self._input_structure),
    autograph=False,
    attributes=defun_kwargs)
def unused(*args):  # pylint: disable=missing-docstring,unused-variable
    ret = wrapper_helper(*args)
    ret = structure.to_tensor_list(self._output_structure, ret)
    exit([ops.convert_to_tensor(t) for t in ret])

_ = unused.get_concrete_function()

def py_function_wrapper(*args):
    nested_args = structure.from_compatible_tensor_list(
        self._input_structure, args)
    if not _should_unpack(nested_args):
        nested_args = (nested_args,)
    ret = self._func(*nested_args)
    if _should_pack(ret):
        ret = tuple(ret)
    ret = structure.to_tensor_list(self._output_structure, ret)
    exit([ops.convert_to_tensor(t) for t in ret])

# Next we trace the function wrapped in `eager_py_func` to force eager
# execution.
@eager_function.defun_with_attributes(
    input_signature=structure.get_flat_tensor_specs(
        self._input_structure),
    autograph=False,
    attributes=defun_kwargs)
def wrapped_fn(*args):  # pylint: disable=missing-docstring
    exit(script_ops.eager_py_func(
        py_function_wrapper, args,
        structure.get_flat_tensor_types(self._output_structure)))

exit(wrapped_fn.get_concrete_function)
