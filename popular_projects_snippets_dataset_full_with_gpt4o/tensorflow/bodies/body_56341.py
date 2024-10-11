# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
# This test needs a placeholder which means we need to construct a graph.
with ops.Graph().as_default():
    unknown = array_ops.placeholder(dtypes.int64, name="unknown")
    partial = array_ops.placeholder(
        dtypes.float32, shape=[None, 1], name="partial")

    spec_1 = tensor_spec.TensorSpec.from_tensor(unknown)
    self.assertEqual(spec_1.dtype, dtypes.int64)
    self.assertEqual(spec_1.shape, None)
    self.assertEqual(spec_1.name, "unknown")
    spec_2 = tensor_spec.TensorSpec.from_tensor(partial)
    self.assertEqual(spec_2.dtype, dtypes.float32)
    self.assertEqual(spec_2.shape.as_list(), [None, 1])
    self.assertEqual(spec_2.name, "partial")
