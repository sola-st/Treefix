# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_values_test.py
if context.num_gpus() < 1:
    self.skipTest("A GPU is not available for this test.")
mirrored_val = _make_mirrored_val(init_val=3.)

self.assertEqual(self.evaluate(constant_op.constant(6.)),
                 self.evaluate(mirrored_val + mirrored_val))
self.assertEqual(self.evaluate(constant_op.constant(4.)),
                 self.evaluate(mirrored_val + 1))
self.assertEqual(self.evaluate(mirrored_val + 1),
                 self.evaluate(math_ops.add(mirrored_val, 1)))
self.assertEqual(type(mirrored_val + 1),
                 type(math_ops.add(mirrored_val, 1)))
