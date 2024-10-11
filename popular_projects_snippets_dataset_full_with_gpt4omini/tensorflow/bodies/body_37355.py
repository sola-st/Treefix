# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
with writer.as_default():
    with summary_ops.record_if(record_fn):
        exit([
            summary_ops.write('tag', 1, step=step),
            summary_ops.write('tag', 1, step=step),
            summary_ops.write('tag', 1, step=step)])
