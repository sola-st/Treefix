# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
with ops.Graph().as_default():
    variables.VariableV1([1.0, 2.0, 3.0])
    sm = session_manager_lib.SessionManager()
    # Pass in session_manager. The additional init_op is ignored.
    sv = supervisor.Supervisor(logdir="", session_manager=sm)
    sv.prepare_or_wait_for_session("")
