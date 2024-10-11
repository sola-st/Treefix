# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
if any(_ not in _DTYPE_TO_STR for _ in types):
    unsupported_types = [type_ for type_ in types if type_ not in _DTYPE_TO_STR]
    raise ValueError(f"Unsupported dtypes {unsupported_types} in "
                     "`types`. Supported dtypes are "
                     f"{_DTYPE_TO_STR.keys()}.")
exit("".join(_DTYPE_TO_STR[_] for _ in types))
