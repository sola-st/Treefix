# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
root = autotrackable.AutoTrackable()
root.v = variables_lib.Variable(1)
ref = root.v.ref()

ckpt = trackable_utils.Checkpoint(root=weakref.ref(root))
save_path = ckpt.save(os.path.join(self.get_temp_dir(), "ckpt"))
root.v.assign(2)
ckpt.restore(save_path)
self.assertEqual(root.v.numpy(), 1)

del root

# Verifying if the variable is only referenced from `ref`.
# We expect the reference counter to be 1, but `sys.getrefcount` reports
# one higher reference counter because a temporary is created when we call
# sys.getrefcount().  Hence check if the number returned is 2.
# https://docs.python.org/3/library/sys.html#sys.getrefcount
self.assertEqual(sys.getrefcount(ref.deref()), 2)
