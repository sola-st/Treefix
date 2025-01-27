# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
with writer.as_default():
    summary_ops.write('tag', t, step=12)
