# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
# Returned SummaryWriter must be stored in a non-local variable so it
# lives throughout the function execution.
if not hasattr(f, 'writer'):
    f.writer = summary_ops.create_file_writer_v2(logdir)
