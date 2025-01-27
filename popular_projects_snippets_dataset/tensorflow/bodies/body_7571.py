# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
# This runs in sub processes, so they are each using their own
# MultiProcessPoolRunner.
_global_pool.run(fn_that_does_nothing)
