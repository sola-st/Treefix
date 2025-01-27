# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec_test.py
desc1 = tensor_spec.TensorSpec([1], dtypes.float32, name="beep")
self.assertEqual(
    repr(desc1), "TensorSpec(shape=(1,), dtype=tf.float32, name='beep')")
desc2 = tensor_spec.TensorSpec([1, None], dtypes.int32)
if desc2.shape._v2_behavior:
    self.assertEqual(
        repr(desc2), "TensorSpec(shape=(1, None), dtype=tf.int32, name=None)")
else:
    self.assertEqual(
        repr(desc2), "TensorSpec(shape=(1, ?), dtype=tf.int32, name=None)")
