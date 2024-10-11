class MockTest: # pragma: no cover
    def getNext(self, dataset): # pragma: no cover
        return iter(dataset) # pragma: no cover
    def assertRaises(self, exception_type): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                if not exc_type or not issubclass(exc_type, exception_type): # pragma: no cover
                    raise AssertionError(f'Expected {exception_type} but got {exc_type}') # pragma: no cover
        return ContextManager() # pragma: no cover
    def evaluate(self, value): # pragma: no cover
        iterator = iter(value) # pragma: no cover
        try: # pragma: no cover
            return next(iterator) # pragma: no cover
        except errors.OutOfRangeError as e: # pragma: no cover
            raise errors.InvalidArgumentError(node_def=None, op=None, message=str(e)) # pragma: no cover
self = MockTest() # pragma: no cover

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
