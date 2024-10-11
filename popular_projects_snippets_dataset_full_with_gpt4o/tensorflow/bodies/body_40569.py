# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
self.assertTrue(context.executing_eagerly())
with ops.init_scope():
    self.assertTrue(context.executing_eagerly())
    context_switches = context.context().context_switches
    self.assertLen(context_switches.stack, 1)
    self.assertFalse(context_switches.stack[0].is_building_function)
    self.assertEqual(context_switches.stack[0].enter_context_fn,
                     context.eager_mode)
