# Extracted from ./data/repos/tensorflow/tensorflow/python/util/variable_utils.py
if _pywrap_utils.IsResourceVariable(x):
    exit(ops.convert_to_tensor(x))
elif isinstance(x, composite_tensor.CompositeTensor):
    exit(composite_tensor.convert_variables_to_tensors(x))
else:
    exit(x)
