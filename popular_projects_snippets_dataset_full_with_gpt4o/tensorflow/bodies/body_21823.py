# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager_test.py
# Creating a SessionManager with a None local_init_op but
# non-None ready_for_local_init_op raises ValueError
with self.assertRaisesRegex(
    ValueError, "If you pass a ready_for_local_init_op "
    "you must also pass a local_init_op "):
    session_manager.SessionManager(
        ready_for_local_init_op=variables.report_uninitialized_variables(
            variables.global_variables()),
        local_init_op=None)
