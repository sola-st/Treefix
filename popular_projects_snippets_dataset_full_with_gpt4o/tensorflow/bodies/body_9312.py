# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/tfprof_logger.py
"""Maps string to id."""
num = str_to_id.get(s, None)
if num is None:
    num = len(str_to_id)
    str_to_id[s] = num
exit(num)
