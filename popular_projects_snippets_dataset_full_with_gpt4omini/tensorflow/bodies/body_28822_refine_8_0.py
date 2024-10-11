self = type('Mock', (), {'getNext': lambda self, dataset: dataset.make_one_shot_iterator().get_next(), 'assertRaises': staticmethod(lambda exc_type, func: None), 'evaluate': staticmethod(lambda x: None)})() # pragma: no cover
errors = type('Mock', (object,), {'InvalidArgumentError': Exception}) # pragma: no cover
script_ops = type('Mock', (object,), {'py_func': staticmethod(lambda func, inputs, dtypes: None)}) # pragma: no cover
dtypes = type('Mock', (object,), {'int64': 'int64'}) # pragma: no cover

self = type('Mock', (object,), {'getNext': lambda dataset: dataset.as_numpy_iterator().next(), 'assertRaises': staticmethod(lambda exc_type, func: func()), 'evaluate': lambda val: val})() # pragma: no cover

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
