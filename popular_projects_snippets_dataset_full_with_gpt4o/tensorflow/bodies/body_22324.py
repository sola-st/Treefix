# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with ops.Graph().as_default(), session_lib.Session() as sess:
    self._validate_print_every_n_steps(sess, at_end=False)
    # Verify proper reset.
    self._validate_print_every_n_steps(sess, at_end=False)
