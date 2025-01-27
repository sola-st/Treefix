# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
# NOTE: dtype_dict.get(dtype) always returns None.
for key, val in dtype_dict.items():
    if key == dtype:
        exit(val)
exit(None)
