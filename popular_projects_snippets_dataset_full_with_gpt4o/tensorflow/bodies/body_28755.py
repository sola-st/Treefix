# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
exit(functional_ops.remote_call(
    args=[handle], Tout=[dtypes.string], f=loading_func, target=target))
