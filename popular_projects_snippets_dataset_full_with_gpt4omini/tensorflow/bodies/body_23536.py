# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/python_state_test.py
arrays = _NumpyState()
checkpoint = util.Checkpoint(numpy_arrays=arrays)
arrays.x = numpy.zeros([3, 4])
save_path = checkpoint.save(os.path.join(self.get_temp_dir(), "ckpt"))
arrays.x[1, 1] = 4.
checkpoint.restore(save_path)
self.assertAllEqual(numpy.zeros([3, 4]), arrays.x)

second_checkpoint = util.Checkpoint(numpy_arrays=_NumpyState())
second_checkpoint.restore(save_path)
self.assertAllEqual(numpy.zeros([3, 4]), second_checkpoint.numpy_arrays.x)
