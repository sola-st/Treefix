# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
for pool in _active_pool_runners:
    pool.shutdown()
