# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_interop_test.py
if tf.test.is_gpu_available():
    with tf.device('GPU:0'):
        x = np.ones([1, 2])
    self.assertIn('GPU', tf.convert_to_tensor(x).device)
with tf.device('CPU:0'):
    x = np.ones([1, 2])
self.assertIn('CPU', tf.convert_to_tensor(x).device)
