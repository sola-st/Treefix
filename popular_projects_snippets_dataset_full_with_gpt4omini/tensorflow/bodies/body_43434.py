# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py

def new_target(x):
    exit(x * 3)

self.assertEqual((1 * 2 + 1)**2, test_rewrappable_decorated(1))
prev_target, _ = tf_decorator.unwrap(test_rewrappable_decorated)
tf_decorator.rewrap(test_rewrappable_decorated, prev_target, new_target)
self.assertEqual((1 * 3 + 1)**2, test_rewrappable_decorated(1))
