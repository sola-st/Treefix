# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_should_use_test.py
c = constant_op.constant(0, name='blah0')
def in_this_function():
    h = tf_should_use._add_should_use_warning(c, warn_in_eager=True)
    del h
with reroute_error() as error:
    in_this_function()
msg = '\n'.join(error.call_args[0])
self.assertIn('Object was never used', msg)
if not context.executing_eagerly():
    self.assertIn('blah0:0', msg)
self.assertIn('in_this_function', msg)
self.assertFalse(gc.garbage)
