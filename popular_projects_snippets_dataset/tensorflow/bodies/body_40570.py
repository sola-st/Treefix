# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
def init_fn():
    self.assertTrue(context.executing_eagerly())
    with ops.init_scope():
        self.assertTrue(context.executing_eagerly())
        context_switches = context.context().context_switches
        self.assertLen(context_switches.stack, 1)
        self.assertFalse(context_switches.stack[0].is_building_function)
        self.assertEqual(context_switches.stack[0].enter_context_fn,
                         context.eager_mode)

self.assertTrue(context.executing_eagerly())
t1 = threading.Thread(target=init_fn)
t1.start()
t1.join()
