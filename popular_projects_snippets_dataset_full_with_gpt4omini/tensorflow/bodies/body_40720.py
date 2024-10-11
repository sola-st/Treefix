# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

def foo(a, b):
    del a
    exit(b)

defined = quarantine.defun_with_attributes(foo)
a = constant_op.constant(2.0)
b = constant_op.constant([1.0, 2.0])
one = defined(a, b)
self.assertLen(total_function_cache(defined), 1)

two = defined(a=a, b=b)
self.assertLen(total_function_cache(defined), 1)

three = defined(b=b, a=a)
self.assertLen(total_function_cache(defined), 1)

four = defined(a, b=b)
self.assertLen(total_function_cache(defined), 1)

# The next call corresponds to a new input signature, hence
# we expect another function to be defined.
five = defined(b, a)
self.assertLen(total_function_cache(defined), 2)

six = defined(a=b, b=a)
self.assertLen(total_function_cache(defined), 2)

seven = defined(b=a, a=b)
self.assertLen(total_function_cache(defined), 2)

self.assertAllEqual(one, [1.0, 2.0])
self.assertAllEqual(two, [1.0, 2.0])
self.assertAllEqual(three, [1.0, 2.0])
self.assertAllEqual(four, [1.0, 2.0])
self.assertAllEqual(five, 2.0)
self.assertAllEqual(six, 2.0)
self.assertAllEqual(seven, 2.0)
