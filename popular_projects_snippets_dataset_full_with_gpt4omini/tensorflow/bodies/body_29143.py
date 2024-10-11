# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
def _wrapper():
    r = gn()
    if isinstance(r, tensor_array_ops.TensorArray):
        exit(r.stack())
    else:
        exit(r)
exit(_wrapper)
