# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
logdir = self._test_dir("prepare_after_stop_chief")
with ops.Graph().as_default():
    sv = supervisor.Supervisor(logdir=logdir, is_chief=True)

    # Create a first session and then stop.
    sess = sv.prepare_or_wait_for_session("")
    sv.stop()
    sess.close()
    self.assertTrue(sv.should_stop())

    # Now create a second session and test that we don't stay stopped, until
    # we ask to stop again.
    sess2 = sv.prepare_or_wait_for_session("")
    self.assertFalse(sv.should_stop())
    sv.stop()
    sess2.close()
    self.assertTrue(sv.should_stop())
