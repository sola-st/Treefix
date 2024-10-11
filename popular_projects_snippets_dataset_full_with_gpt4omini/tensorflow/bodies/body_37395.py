# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
if not hasattr(f1, 'writer'):
    f1.writer = summary_ops.create_file_writer_v2(logdir)
with f1.writer.as_default():
    summary_ops.write('tag', 1, step=1)
