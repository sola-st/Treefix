# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

fn = quarantine.defun_with_attributes(lambda x: 2. * x)

fn(constant_op.constant(4.0))
weak_fn = weakref.ref(fn)
del fn
# Tests that the weak reference we made to the function is now dead, which
# means the object has been deleted. This should be true as long as the
# function itself is not involved in a reference cycle.
self.assertIs(None, weak_fn())
