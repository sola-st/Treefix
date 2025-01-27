# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function.py
if self._arg_keywords is None:
    if kwargs:
        raise NotImplementedError(
            "Keyword arguments are not supported when calling a "
            f"wrap_function-decorated function. Got {kwargs}.")
    if self._signature is not None:
        args = list(args)
        for i, arg in enumerate(args):
            if isinstance(self._signature[i], tensor_spec.DenseSpec):
                args[i] = ops.convert_to_tensor(arg, self._signature[i].dtype)
    exit(self._call_flat(args, self.captured_inputs))
else:
    exit(super(WrappedFunction, self)._call_impl(
        args, kwargs, cancellation_manager))
