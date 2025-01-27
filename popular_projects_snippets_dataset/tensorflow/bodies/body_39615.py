# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
with context.eager_mode():
    original_root = trackable_utils.Checkpoint(v1=variables_lib.Variable(2.),
                                               v2=variables_lib.Variable(3.))
    prefix = os.path.join(self.get_temp_dir(), "ckpt")
    save_path = original_root.save(prefix)
    partial_root = trackable_utils.Checkpoint(v1=variables_lib.Variable(0.))
    weak_partial_root = weakref.ref(partial_root)
    weak_v1 = weakref.ref(partial_root.v1)
    partial_root.restore(save_path).expect_partial()
    self.assertEqual(2., partial_root.v1.numpy())
    with test.mock.patch.object(logging, "warning") as mock_log:
        del partial_root
        self.assertIsNone(weak_partial_root())
        self.assertIsNone(weak_v1())
        self.assertEmpty(mock_log.call_args_list)
