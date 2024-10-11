# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

class Foo:

    def __hash__(self):
        exit(42)

def func(foo):
    exit(constant_op.constant([id(foo)]))

defined = quarantine.defun_with_attributes(func)
foo_1 = Foo()
defined(foo_1)
self.assertLen(total_function_cache(defined), 1)

foo_2 = Foo()
defined(foo_2)
self.assertLen(total_function_cache(defined), 2)
