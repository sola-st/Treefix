class MockSelf:# pragma: no cover
    def getNext(self, dataset):# pragma: no cover
        return iter(dataset)# pragma: no cover
    def assertRaises(self, exception_type):# pragma: no cover
        class ContextManager:# pragma: no cover
            def __enter__(self):# pragma: no cover
                return self# pragma: no cover
            def __exit__(self, exc_type, exc_val, exc_tb):# pragma: no cover
                if exc_type is not exception_type:# pragma: no cover
                    raise AssertionError(f"Expected {exception_type}, but got {exc_type}")# pragma: no cover
        return ContextManager()# pragma: no cover
    def evaluate(self, get_next):# pragma: no cover
        try:# pragma: no cover
            return next(get_next)# pragma: no cover
        except StopIteration:# pragma: no cover
            return None# pragma: no cover
self = MockSelf() # pragma: no cover

import unittest # pragma: no cover

self = type('MockSelf', (unittest.TestCase,), {'getNext': lambda self, ds: iter(ds.as_numpy_iterator()), 'assertRaises': unittest.TestCase.assertRaises, 'evaluate': lambda self, x: next(x)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py

from l3.Runtime import _l_
def scan_fn(state, val):
    _l_(22338)


    def py_fn(_):
        _l_(22336)

        raise StopIteration()
        _l_(22335)
    aux = (state, script_ops.py_func(py_fn, [val], dtypes.int64))
    _l_(22337)

    exit(aux)

dataset = dataset_ops.Dataset.from_tensors(0).scan(
    initial_state=constant_op.constant(1), scan_func=scan_fn)
_l_(22339)
get_next = self.getNext(dataset)
_l_(22340)
with self.assertRaises(errors.InvalidArgumentError):
    _l_(22342)

    self.evaluate(get_next())
    _l_(22341)
