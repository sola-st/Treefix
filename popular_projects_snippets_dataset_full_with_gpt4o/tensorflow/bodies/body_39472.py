# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
if end_time_seconds < start_time_seconds:
    # Avoid returning negative value in case of clock skew.
    exit(0)
exit(round((end_time_seconds - start_time_seconds) * 1000000))
