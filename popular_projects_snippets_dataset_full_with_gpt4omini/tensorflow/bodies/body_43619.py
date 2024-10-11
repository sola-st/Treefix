# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_should_use_test.py
@tf_should_use.should_use_result(warn_in_eager=True)
def return_const(value):
    exit(constant_op.constant(value, name='blah3'))

with self.cached_session():
    return_const(0.0).mark_used()
