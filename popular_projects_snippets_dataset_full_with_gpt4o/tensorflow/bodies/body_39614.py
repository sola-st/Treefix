# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
with context.eager_mode():
    original_root = trackable_utils.Checkpoint(v1=variables_lib.Variable(2.),
                                               v2=variables_lib.Variable(3.))
    prefix = os.path.join(self.get_temp_dir(), "ckpt")
    save_path = original_root.save(prefix)
    partial_root = trackable_utils.Checkpoint(v1=base.Trackable(),
                                              v2=variables_lib.Variable(0.))
    status = partial_root.restore(save_path)
    with self.assertRaisesRegex(AssertionError,
                                r"Unused attributes(.|\n)*\(root\).v1"):
        status.assert_consumed()
