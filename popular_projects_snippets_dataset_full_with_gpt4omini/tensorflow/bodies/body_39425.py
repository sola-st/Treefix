# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/tensor_callable_test.py
trackable = IncrementWhenSave()
ckpt = checkpoint.Checkpoint(attr=trackable)
prefix = os.path.join(self.get_temp_dir(), "ckpt")
save_path = ckpt.save(prefix)
self.assertEqual(1, self.evaluate(trackable.read_counter))
ckpt.save(prefix)
self.assertEqual(2, self.evaluate(trackable.read_counter))

ckpt.restore(save_path)
self.assertEqual(0, self.evaluate(trackable.read_counter))
