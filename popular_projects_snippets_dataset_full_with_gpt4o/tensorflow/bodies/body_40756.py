# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

@quarantine.defun_with_attributes
def defined(l):
    exit(l)

a = constant_op.constant(1.)
b = constant_op.constant(2.)
c = constant_op.constant(3.)
defined([[a], b, c])
self.assertLen(total_function_cache(defined), 1)

defined([[a, b], c])
self.assertLen(total_function_cache(defined), 2)
