# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test.py
"""Test that control_flow_util can check that we're in a TPU context."""
with ops.Graph().as_default():
    z1 = array_ops.identity(1)
    pivot = control_flow_ops.no_op()
    context = tpu.TPUReplicateContext(b"context", 1, pivot=pivot)
    context.Enter()
    z2 = array_ops.identity(1)
    context.Exit()
    self.assertFalse(control_flow_util.IsInXLAContext(z1.op))
    self.assertTrue(control_flow_util.IsInXLAContext(z2.op))
