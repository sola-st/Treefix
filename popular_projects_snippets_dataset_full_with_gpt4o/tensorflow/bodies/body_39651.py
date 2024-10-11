# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
root = autotrackable.AutoTrackable()
root.v = variables_lib.Variable(1)
w = variables_lib.Variable(2)
y = variables_lib.Variable(3)
root_ckpt = trackable_utils.Checkpoint(root=root, w=w, y=y)

root2 = autotrackable.AutoTrackable()
root2.w = variables_lib.Variable(4)
v2 = variables_lib.Variable(5)
z = variables_lib.Variable(6)
root2_ckpt = trackable_utils.Checkpoint(root=root2,
                                        v=v2,
                                        z=z)

root_save_path = root_ckpt.save(os.path.join(self.get_temp_dir(),
                                             "root_ckpt"))
root2_save_path = root2_ckpt.save(os.path.join(self.get_temp_dir(),
                                               "root2_ckpt"))

root_ckpt.restore(root2_save_path)
root2_ckpt.restore(root_save_path)

self.assertEqual(root.v.numpy(), 5)
self.assertEqual(w.numpy(), 4)
self.assertEqual(y.numpy(), 3)

self.assertEqual(root2.w.numpy(), 2)
self.assertEqual(v2.numpy(), 1)
self.assertEqual(z.numpy(), 6)
