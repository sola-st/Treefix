# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/composite_tensor_test.py
with self.assertRaises((TypeError, ValueError)):  # pylint: disable=g-error-prone-assert-raises
    nest.assert_shallow_structure(
        s1, s2, expand_composites=True, check_types=check_types)
