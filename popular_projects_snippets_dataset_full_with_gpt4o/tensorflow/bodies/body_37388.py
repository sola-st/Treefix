# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
with summary_ops.create_file_writer_v2(logdir).as_default():
    pass  # Calling .as_default() is enough to indicate use.
