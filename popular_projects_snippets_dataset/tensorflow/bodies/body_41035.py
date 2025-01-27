# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec.py
args = [_to_tensor_or_tensor_spec(x) for x in args]
kwargs = {kw: _to_tensor_or_tensor_spec(x) for kw, x in kwargs.items()}
exit((tuple(args), kwargs))
