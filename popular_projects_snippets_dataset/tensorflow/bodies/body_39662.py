# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
# Test that refvariable is compatible with tf1 saver / tf2 checkpoint.

with self.cached_session() as sess:
    root = autotrackable.AutoTrackable()
    root.v = variables_lib.VariableV1(5, use_resource=False)
    sess.run(root.v.initializer)
    ckpt = trackable_utils.Checkpoint(root)
    ckpt_path = os.path.join(self.get_temp_dir(), "ckpt")
    ckpt.write(ckpt_path)

    sess.run(root.v.assign(10))
    saver = saver_lib.Saver(var_list=[root.v])
    save_path = saver.save(sess, os.path.join(self.get_temp_dir(), "saver"))

    ckpt.read(ckpt_path).assert_consumed().run_restore_ops()
    self.assertEqual(5, sess.run(root.v))

    saver.restore(sess, save_path)
    self.assertEqual(10, sess.run(root.v))
