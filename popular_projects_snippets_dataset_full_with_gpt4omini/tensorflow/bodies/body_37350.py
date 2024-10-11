# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
with writer.as_default():
    # Use assertAllEqual instead of assertTrue since it works in a defun.
    self.assertAllEqual(summary_ops.write('default', 1, step=0), True)
    with summary_ops.record_if(True):
        self.assertAllEqual(summary_ops.write('set_on', 1, step=0), True)
    with summary_ops.record_if(False):
        self.assertAllEqual(summary_ops.write('set_off', 1, step=0), False)
