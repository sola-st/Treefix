# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
v = variables.Variable(1.)
l = data_structures.ListWrapper([1, 2, 3, 4, v])
self.assertDictEqual({"4": v}, l._trackable_children())
root = util.Checkpoint(l=l)
prefix = os.path.join(self.get_temp_dir(), "ckpt")
path = root.save(prefix)
v.assign(5.)
l *= 2
self.assertEqual(l, [1, 2, 3, 4, v, 1, 2, 3, 4, v])
self.assertDictEqual({"4": v, "9": v}, l._trackable_children())
root.restore(path)
self.assertAllClose(1., v.numpy())
