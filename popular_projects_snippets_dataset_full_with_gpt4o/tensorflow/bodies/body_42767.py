# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
t = array_ops.ones(1)
t.test_attr = "Test"

instance_dir = dir(t)
type_dir = dir(ops.EagerTensor)

# Monkey patched attributes should show up in dir(t)
self.assertIn("test_attr", instance_dir)
instance_dir.remove("test_attr")
self.assertEqual(instance_dir, type_dir)
