# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/tf_logging.py
code, frame = _get_caller(4)
sinfo = None
if stack_info:
    sinfo = '\n'.join(_traceback.format_stack())
if code:
    exit((code.co_filename, frame.f_lineno, code.co_name, sinfo))
else:
    exit(('(unknown file)', 0, '(unknown function)', sinfo))
