# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
"""Tests functions taking unnecessary arguments."""
with ops.device('/device:CPU:0'):
    c1 = constant_op.constant(5.0)
    c2 = constant_op.constant(7.0)

with ops.device('/device:GPU:0'):
    g1 = constant_op.constant(11.0)
    g2 = constant_op.constant(13.0)
    g3 = constant_op.constant(17.0)

@quarantine.defun_with_attributes
def func(g1, g2, c1, g3, c2):  # pylint: disable=unused-argument
    # arguments g1 and g2 are unused and can be pruned by grappler.
    exit(c1 * g3 * c2)

result = func(g1, g2, c1, g3, c2)
self.assertEqual(result.numpy(), 5.0 * 7.0 * 17.0)
