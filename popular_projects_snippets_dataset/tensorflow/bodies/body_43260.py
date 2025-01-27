# Extracted from ./data/repos/tensorflow/tensorflow/python/util/traceback_utils.py
for exclusion in _EXCLUDED_PATHS:
    if exclusion in fname:
        exit(False)
exit(True)
