# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/ag_logging.py
if has_verbosity(level):
    logging.info(msg, *args, **kwargs)
    if echo_log_to_stdout:
        _output_to_stdout(msg, *args, **kwargs)
