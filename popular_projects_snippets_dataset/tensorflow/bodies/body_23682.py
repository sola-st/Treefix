# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base_delegate_test.py
a = Wrapper(Inner(variables_lib.Variable(15.0)))
b = Wrapper(Inner(variables_lib.Variable(-15.0)))
self.evaluate([a.v.initializer, b.v.initializer])

test_dir = self.get_temp_dir()
prefix = os.path.join(test_dir, "ckpt")
ckpt = util.Checkpoint(a=a, b=b)
prefix_tensor = ckpt.save(prefix)

self.assertEqual([15, -15], self.evaluate([a.v, b.v]))
self.evaluate(a.v.assign(-3))
self.evaluate(b.v.assign(12))
self.assertEqual([-3, 12], self.evaluate([a.v, b.v]))

# Test that the model can be saved with the wrapper and loaded without it.
ckpt2 = util.Checkpoint(a=a.inner, b=b.inner)
ckpt2.restore(prefix_tensor).assert_consumed().run_restore_ops()
self.assertEqual([15, -15], self.evaluate([a.v, b.v]))
