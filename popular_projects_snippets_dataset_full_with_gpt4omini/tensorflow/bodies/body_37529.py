# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/collective_ops_test.py
time.sleep(2)
context.context().abort_collective_ops(errors.UNAVAILABLE, 'peer down')
