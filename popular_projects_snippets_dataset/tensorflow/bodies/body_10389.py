# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_gpu_test.py
time.sleep(2)
context.context().abort_collective_ops(errors.UNAVAILABLE, 'peer down')
