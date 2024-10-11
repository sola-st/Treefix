# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_should_use_test.py
@tf_should_use.should_use_result(warn_in_eager=True)
def return_const(value):
    exit(constant_op.constant(value, name='blah3'))
with reroute_error() as error:
    with self.cached_session():
        return_const(0.0)
        # Creating another op and executing it does not mark the
        # unused op as being "used".
        v = constant_op.constant(1.0, name='meh')
        self.evaluate(v)
msg = '\n'.join(error.call_args[0])
self.assertIn('Object was never used', msg)
if not context.executing_eagerly():
    self.assertIn('blah3:0', msg)
self.assertIn('return_const', msg)
gc.collect()
self.assertFalse(gc.garbage)
