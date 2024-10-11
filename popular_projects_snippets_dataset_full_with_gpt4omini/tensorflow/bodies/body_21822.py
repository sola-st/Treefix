# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager_test.py
with ops.Graph().as_default():
    variables.VariableV1(1, name="v")
    sm = session_manager.SessionManager(
        ready_op=variables.report_uninitialized_variables(),
        recovery_wait_secs=1)

    # Set max_wait_secs to allow us to try a few times.
    with self.assertRaises(errors.DeadlineExceededError):
        sm.wait_for_session(master="", max_wait_secs=3)
