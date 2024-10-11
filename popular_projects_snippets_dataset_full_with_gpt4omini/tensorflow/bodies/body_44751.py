# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/ag_logging.py
if has_verbosity(level):
    logging.error(msg, *args, **kwargs)
    if echo_log_to_stdout:
        _output_to_stdout('ERROR: ' + msg, *args, **kwargs)
