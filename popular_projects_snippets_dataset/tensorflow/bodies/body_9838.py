# Extracted from ./data/repos/tensorflow/tensorflow/python/dlpack/dlpack_test.py
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "The argument to `to_dlpack` must be a TF tensor, not Python object"):
    dlpack.to_dlpack([1])
