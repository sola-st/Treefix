# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/python_state_test.py
directory = self.get_temp_dir()
prefix = os.path.join(directory, "ckpt")
root = util.Checkpoint(numpy=_NumpyWrapper(numpy.array([1.])))
save_path = root.save(prefix)
root.numpy.array *= 2.
self.assertEqual([2.], root.numpy.array)
root.restore(save_path)
self.assertEqual([1.], root.numpy.array)
