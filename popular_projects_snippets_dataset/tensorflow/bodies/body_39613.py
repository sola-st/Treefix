# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
with context.eager_mode():
    original_root = trackable_utils.Checkpoint(v1=variables_lib.Variable(2.),
                                               v2=variables_lib.Variable(3.))
    prefix = os.path.join(self.get_temp_dir(), "ckpt")
    save_path = original_root.save(prefix)
    partial_root = trackable_utils.Checkpoint(v1=base.Trackable(),
                                              v2=variables_lib.Variable(0.))
    weak_partial_root = weakref.ref(partial_root)
    with test.mock.patch.object(logging, "warning") as mock_log:
        # Note: Unlike in testPartialRestoreWarningObject, the warning actually
        # prints immediately here, since all of the objects have been created
        # and there's no deferred restoration sitting around.
        partial_root.restore(save_path)
        self.assertEqual(3., partial_root.v2.numpy())
        del partial_root
        self.assertIsNone(weak_partial_root())
        messages = str(mock_log.call_args_list)
    self.assertIn("(root).v1", messages)
    self.assertNotIn("(root).v2", messages)
    self.assertIn("expect_partial()", messages)
