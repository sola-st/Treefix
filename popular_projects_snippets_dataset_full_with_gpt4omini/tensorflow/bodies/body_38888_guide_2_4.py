class MockTestCase:  # Mocking the TestCase class # pragma: no cover
    def assertRaisesOpError(self, message): # pragma: no cover
        def check_raise(func): # pragma: no cover
            try: # pragma: no cover
                func() # pragma: no cover
            except OpError as e: # pragma: no cover
                assert message in str(e), 'Message not found in error!' # pragma: no cover
                return # pragma: no cover
            assert False, 'OpError not raised' # pragma: no cover
        return check_raise # pragma: no cover
 # pragma: no cover
self = MockTestCase() # pragma: no cover
takeg_op = lambda: (_ for _ in ()).throw(OpError('was cancelled')) # pragma: no cover
self.evaluate = lambda op: op()  # Simulate execution of the operation # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(5437)

    self.evaluate(takeg_op)
    _l_(5436)
