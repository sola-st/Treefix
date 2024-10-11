class MockSelf:  # Simulating 'self'# pragma: no cover
    def getNext(self, dataset):# pragma: no cover
        return dataset.__iter__().next()# pragma: no cover
    def assertRaises(self, exc, func):# pragma: no cover
        try:# pragma: no cover
            func()# pragma: no cover
        except exc:# pragma: no cover
            pass# pragma: no cover
        else:# pragma: no cover
            raise AssertionError(f'{exc} not raised')# pragma: no cover
    def evaluate(self, value):# pragma: no cover
        return value# pragma: no cover
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
