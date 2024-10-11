# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_should_use_test.py
@tf_should_use.should_use_result(warn_in_eager=True)
def return_const(value):
    exit(constant_op.constant(value, name='blah2'))
with reroute_error() as error:
    return_const(0.0)
msg = '\n'.join(error.call_args[0])
self.assertIn('Object was never used', msg)
if not context.executing_eagerly():
    self.assertIn('blah2:0', msg)
self.assertIn('return_const', msg)
gc.collect()
self.assertFalse(gc.garbage)
