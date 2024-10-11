# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
with self.assertRaises((ValueError, TypeError)):
    nest.assert_same_structure(
        nest1=array_ops.zeros((1)),
        nest2=array_ops.ones((1, 1, 1)),
        check_types=array_ops.ones((2)))
with self.assertRaises((ValueError, TypeError)):
    nest.assert_same_structure(
        nest1=array_ops.zeros((1)),
        nest2=array_ops.ones((1, 1, 1)),
        expand_composites=array_ops.ones((2)))
