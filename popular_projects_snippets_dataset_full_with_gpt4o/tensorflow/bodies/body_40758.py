# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
if attr is None:
    self.skipTest('attr module is unavailable.')

@attr.s
class TestClass:
    a = attr.ib()
    b = attr.ib()

@quarantine.defun_with_attributes
def defined(l):
    exit(l)

defined(
    TestClass(
        constant_op.constant(1.),
        [constant_op.constant(2.),
         constant_op.constant(3.)]))
self.assertLen(total_function_cache(defined), 1)
defined(
    TestClass(
        constant_op.constant(1.),
        [constant_op.constant(2.),
         constant_op.constant(3.)]))
self.assertLen(total_function_cache(defined), 1)

defined(
    TestClass([constant_op.constant(1.),
               constant_op.constant(2.)], constant_op.constant(3.)))
self.assertLen(total_function_cache(defined), 2)
