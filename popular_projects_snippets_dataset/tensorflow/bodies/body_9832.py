# Extracted from ./data/repos/tensorflow/tensorflow/python/dlpack/dlpack_test.py
np.random.seed(42)
np_array = np.random.randint(0, 10, shape)
# copy to gpu if available
tf_tensor = array_ops.identity(constant_op.constant(np_array, dtype=dtype))
tf_tensor_device = tf_tensor.device
tf_tensor_dtype = tf_tensor.dtype
dlcapsule = dlpack.to_dlpack(tf_tensor)
del tf_tensor  # should still work
tf_tensor2 = dlpack.from_dlpack(dlcapsule)
self.assertAllClose(np_array, tf_tensor2)
if tf_tensor_dtype == dtypes.int32:
    # int32 tensor is always on cpu for now
    self.assertEqual(tf_tensor2.device,
                     "/job:localhost/replica:0/task:0/device:CPU:0")
else:
    self.assertEqual(tf_tensor_device, tf_tensor2.device)
