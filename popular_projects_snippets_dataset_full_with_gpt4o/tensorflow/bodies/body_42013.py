# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/device_placement_test.py
with ops.device('GPU:0'):
    t = constant_op.constant([[1, 2], [3, 4]])
    a = math_ops.add(array_ops.shape(t),
                     constant_op.constant([10, 20], dtype=dtypes.int32))
# Shape computations remain on CPU
self.assertIn('CPU:0', a.backing_device)
