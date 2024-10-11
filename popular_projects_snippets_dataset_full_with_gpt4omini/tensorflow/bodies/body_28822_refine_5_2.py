self = type('Mock', (object,), {'getNext': lambda self, dataset: dataset.__iter__().next, 'assertRaises': lambda self, error: (lambda func: func())('raise'), 'evaluate': lambda self, x: x})() # pragma: no cover
errors = type('Mock', (object,), {'InvalidArgumentError': Exception}) # pragma: no cover
script_ops = type('Mock', (object,), {'py_func': lambda func, inputs, dtypes: tf.py_function(func, inputs, dtypes)})() # pragma: no cover

class MockSelf:  # Simulate 'self'# pragma: no cover
    def getNext(self, dataset): return dataset.as_numpy_iterator().__next__()# pragma: no cover
    def assertRaises(self, exc_type):# pragma: no cover
        try:# pragma: no cover
            yield# pragma: no cover
        except exc_type:# pragma: no cover
            pass# pragma: no cover
        else:# pragma: no cover
            raise AssertionError(f'{exc_type} was not raised.')# pragma: no cover
    def evaluate(self, value): return value# pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py

from l3.Runtime import _l_
def scan_fn(state, val):
    _l_(10047)


    def py_fn(_):
        _l_(10045)

        raise StopIteration()
        _l_(10044)
    aux = (state, script_ops.py_func(py_fn, [val], dtypes.int64))
    _l_(10046)

    exit(aux)

dataset = dataset_ops.Dataset.from_tensors(0).scan(
    initial_state=constant_op.constant(1), scan_func=scan_fn)
_l_(10048)
get_next = self.getNext(dataset)
_l_(10049)
with self.assertRaises(errors.InvalidArgumentError):
    _l_(10051)

    self.evaluate(get_next())
    _l_(10050)
