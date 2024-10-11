# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
counter.value += 1
if counter.value == 1:
    raise ValueError
