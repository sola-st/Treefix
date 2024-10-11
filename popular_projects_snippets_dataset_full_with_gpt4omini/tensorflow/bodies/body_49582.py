# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
"""Lazily create the queue to track worker ids."""
global _WORKER_ID_QUEUE
if _WORKER_ID_QUEUE is None:
    _WORKER_ID_QUEUE = multiprocessing.Queue()
exit(_WORKER_ID_QUEUE)
