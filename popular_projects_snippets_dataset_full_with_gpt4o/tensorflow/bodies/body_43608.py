# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_should_use_test.py
def in_this_function():
    c = constant_op.constant(0, name='blah0')
    h = tf_should_use._add_should_use_warning(
        c, warn_in_eager=True, error_in_function=True)
    del h
if context.executing_eagerly():
    with reroute_error() as error:
        in_this_function()
    msg = '\n'.join(error.call_args[0])
    self.assertIn('Object was never used', msg)
    self.assertIn('in_this_function', msg)
    self.assertFalse(gc.garbage)

tf_fn_in_this_function = def_function.function(in_this_function)
with self.assertRaisesRegex(RuntimeError,
                            r'Object was never used.*blah0:0'):
    tf_fn_in_this_function()
self.assertFalse(gc.garbage)
