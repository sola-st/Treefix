# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
global V
old_val = V
V = val
exit(old_val)
