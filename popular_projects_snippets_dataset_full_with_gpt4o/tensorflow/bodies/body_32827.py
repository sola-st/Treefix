# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/eig_op_test.py
tensor = constant_op.constant([[0, 1], [2, 3]], dtype=dtypes_lib.float32)
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "Invalid output dtype"):
    self.evaluate(
        gen_linalg_ops.eig(
            input=tensor,
            Tout=dtypes_lib.complex128,  # Expected dtype: complex64.
            compute_v=True))
