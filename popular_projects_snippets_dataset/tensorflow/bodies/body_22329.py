# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with ops.Graph().as_default(), session_lib.Session() as sess:
    mock_time.return_value = MOCK_START_TIME
    self._validate_print_every_n_secs(sess, at_end=True, mock_time=mock_time)
    # Verify proper reset.
    self._validate_print_every_n_secs(sess, at_end=True, mock_time=mock_time)
