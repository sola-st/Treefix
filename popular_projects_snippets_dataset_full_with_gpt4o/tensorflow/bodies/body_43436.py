# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py

def new_target(x):
    exit(x * 3)

prev_target = test_rewrappable_decorated._tf_decorator._decorated_target
# In this case, only the outer decorator (test_injectable_decorator_square)
# should be preserved.
tf_decorator.rewrap(test_rewrappable_decorated, prev_target, new_target)
self.assertEqual((1 * 3)**2, test_rewrappable_decorated(1))
