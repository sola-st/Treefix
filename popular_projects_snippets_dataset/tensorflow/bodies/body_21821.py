# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager_test.py
# Create a checkpoint.
checkpoint_dir = os.path.join(self.get_temp_dir(), "recover_session")
try:
    gfile.DeleteRecursively(checkpoint_dir)
except errors.OpError:
    pass  # Ignore
gfile.MakeDirs(checkpoint_dir)

with ops.Graph().as_default():
    v = variables.VariableV1(1, name="v")
    sm = session_manager.SessionManager(
        ready_op=variables.report_uninitialized_variables())
    saver = saver_lib.Saver({"v": v})
    sess, initialized = sm.recover_session(
        "", saver=saver, checkpoint_dir=checkpoint_dir)
    self.assertFalse(initialized)
    sess.run(v.initializer)
    self.assertEqual(1, sess.run(v))
    saver.save(sess, os.path.join(checkpoint_dir,
                                  "recover_session_checkpoint"))
self._test_recovered_variable(checkpoint_dir=checkpoint_dir)
self._test_recovered_variable(
    checkpoint_filename_with_path=checkpoint_management.latest_checkpoint(
        checkpoint_dir))
# Cannot set both checkpoint_dir and checkpoint_filename_with_path.
with self.assertRaises(ValueError):
    self._test_recovered_variable(
        checkpoint_dir=checkpoint_dir,
        checkpoint_filename_with_path=checkpoint_management.latest_checkpoint(
            checkpoint_dir))
