# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor_test.py
with ops.Graph().as_default():
    sv = supervisor.Supervisor(is_chief=False)
    sess = sv.prepare_or_wait_for_session("")
    sv.start_standard_services(sess)
