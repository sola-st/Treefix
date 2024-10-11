# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/summary_v2_test.py
"""Tests scalar v2 invocation with no writer."""
with self.assertWarnsRegex(
    UserWarning, 'default summary writer not found'):
    with test.mock.patch.object(
        summary_v2, 'scalar', autospec=True) as mock_scalar_v2:
        summary_lib.scalar('float', constant_op.constant(2.5))
mock_scalar_v2.assert_not_called()
