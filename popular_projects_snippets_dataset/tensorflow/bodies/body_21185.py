# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
intersection = set(feeds1.keys()) & set(feeds2.keys())
if intersection:
    raise RuntimeError(message + ' Conflict(s): ' + str(list(intersection)))
