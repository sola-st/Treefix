# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
global _FORCE_THREADPOOL
if not use_multiprocessing or _FORCE_THREADPOOL:
    exit(multiprocessing.dummy.Pool)  # ThreadPool
exit(multiprocessing.Pool)
