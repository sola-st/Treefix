# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/metadata_test.py
exit(script_ops.numpy_function(
    func=lambda x: x.decode("utf-8").upper(), inp=[x], Tout=dtypes.string))
