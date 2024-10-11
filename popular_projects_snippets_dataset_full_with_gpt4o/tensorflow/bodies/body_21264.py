# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
with ops.Graph().as_default():
    variables.VariableV1([1.0, 2.0, 3.0])
    sv = supervisor.Supervisor(logdir="", summary_op=None)
    sess = sv.prepare_or_wait_for_session("")
    sess.close()
    sv.stop()
