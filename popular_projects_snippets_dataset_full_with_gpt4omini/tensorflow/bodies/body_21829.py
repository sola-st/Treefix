# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager_test.py
with ops.Graph().as_default() as graph:
    v = variables.VariableV1(1, name="v")
    w = variables.VariableV1(
        v,
        trainable=False,
        collections=[ops.GraphKeys.LOCAL_VARIABLES],
        name="w")
    sm = session_manager.SessionManager(
        graph=graph,
        ready_op=variables.report_uninitialized_variables(),
        ready_for_local_init_op=variables.report_uninitialized_variables(),
        local_init_op=w.initializer)

    with self.assertRaises(errors_impl.DeadlineExceededError):
        # Time-out because w fails to be initialized,
        # because of overly restrictive ready_for_local_init_op
        sm.wait_for_session("", max_wait_secs=3)
