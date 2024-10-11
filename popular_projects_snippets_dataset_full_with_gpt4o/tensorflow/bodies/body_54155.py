# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/composite_tensor_test.py
# s1 and s2 have the same structure if expand_composites=False; but
# different structures if expand_composites=True.
nest.assert_same_structure(s1, s2, expand_composites=False)
nest.assert_shallow_structure(s1, s2, expand_composites=False)
with self.assertRaises(error):  # pylint: disable=g-error-prone-assert-raises
    nest.assert_same_structure(s1, s2, expand_composites=True)
