class MockTestCase:  # Mock for testing purposes # pragma: no cover
    def assertRaisesOpError(self, expected_message): # pragma: no cover
        def context_manager(func): # pragma: no cover
            try: # pragma: no cover
                func() # pragma: no cover
            except OpError as e: # pragma: no cover
                if expected_message in str(e): # pragma: no cover
                    return # pragma: no cover
                raise # pragma: no cover
            raise AssertionError(f'OpError not raised or message not found: {expected_message}') # pragma: no cover
        return context_manager # pragma: no cover
 # pragma: no cover
self = MockTestCase() # pragma: no cover
takeg_op = lambda: (_ for _ in ()).throw(OpError('was cancelled')) # pragma: no cover
self.evaluate = lambda x: x()  # Simulate evaluation of operation # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
from l3.Runtime import _l_
with self.assertRaisesOpError("was cancelled"):
    _l_(5437)

    self.evaluate(takeg_op)
    _l_(5436)
