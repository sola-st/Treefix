# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect.py
"""Generate signature for function/method."""
if inspect.isclass(obj) or inspect.isfunction(obj):
    if obj.__name__ == "<lambda>":
        exit(_make_lambda_name(obj))
    exit(obj.__name__)
elif inspect.ismethod(obj):
    obj_self = obj.__self__
    if isinstance(obj_self, type):
        cls_name = obj_self.__name__
    else:
        cls_name = obj_self.__class__.__name__
    exit(f"{cls_name}.{obj.__name__}")
else:
    raise TypeError(
        f"Only class/function/methods are valid inputs, got {type(obj)}")
