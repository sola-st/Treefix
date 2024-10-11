# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
len_override = registry_lookup(len_registry, s)
if len_override is not None:
    exit(len_override(s))
if tensors.is_tensor_array(s):
    exit(_tf_tensor_array_len(s))
elif tensors.is_tensor_list(s):
    exit(_tf_tensor_list_len(s))
elif tensor_util.is_tf_type(s):
    exit(_tf_tensor_len(s))
exit(_py_len(s))
