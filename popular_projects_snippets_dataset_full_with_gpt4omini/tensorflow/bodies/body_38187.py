# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
x = array_ops.placeholder(dtypes_lib.string)
with self.assertRaisesRegex(TypeError,
                            r"Expected numeric or variant tensor"):
    math_ops.conj(x)
