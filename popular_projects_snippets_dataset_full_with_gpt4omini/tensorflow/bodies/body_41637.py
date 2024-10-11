# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
has_decorated_method = _HasDecoratedMethod()
has_decorated_method.f(constant_op.constant(5.))
weak_fn = weakref.ref(has_decorated_method.f)
del has_decorated_method
# Tests that the weak reference we made to the function is now dead, which
# means the object has been deleted. This should be true as long as the
# function itself is not involved in a reference cycle.
self.assertIs(None, weak_fn())
