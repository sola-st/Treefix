# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
# This test needs a placeholder which means we need to construct a graph.
with ops.Graph().as_default():
    unknown = array_ops.placeholder(dtypes.int64)
    partial = array_ops.placeholder(dtypes.int64, shape=[None, 1])
    full = array_ops.placeholder(dtypes.int64, shape=[2, 3])
    rank3 = array_ops.placeholder(dtypes.int64, shape=[4, 5, 6])

    desc_unknown = tensor_spec.TensorSpec(None, dtypes.int64)
    self.assertTrue(desc_unknown.is_compatible_with(unknown))
    self.assertTrue(desc_unknown.is_compatible_with(partial))
    self.assertTrue(desc_unknown.is_compatible_with(full))
    self.assertTrue(desc_unknown.is_compatible_with(rank3))

    desc_partial = tensor_spec.TensorSpec([2, None], dtypes.int64)
    self.assertTrue(desc_partial.is_compatible_with(unknown))
    self.assertTrue(desc_partial.is_compatible_with(partial))
    self.assertTrue(desc_partial.is_compatible_with(full))
    self.assertFalse(desc_partial.is_compatible_with(rank3))

    desc_full = tensor_spec.TensorSpec([2, 3], dtypes.int64)
    self.assertTrue(desc_full.is_compatible_with(unknown))
    self.assertFalse(desc_full.is_compatible_with(partial))
    self.assertTrue(desc_full.is_compatible_with(full))
    self.assertFalse(desc_full.is_compatible_with(rank3))

    desc_rank3 = tensor_spec.TensorSpec([4, 5, 6], dtypes.int64)
    self.assertTrue(desc_rank3.is_compatible_with(unknown))
    self.assertFalse(desc_rank3.is_compatible_with(partial))
    self.assertFalse(desc_rank3.is_compatible_with(full))
    self.assertTrue(desc_rank3.is_compatible_with(rank3))
