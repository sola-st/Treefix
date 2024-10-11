# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/ag_logging.py
logging.warning(msg, *args, **kwargs)
if echo_log_to_stdout:
    _output_to_stdout('WARNING: ' + msg, *args, **kwargs)
    sys.stdout.flush()
