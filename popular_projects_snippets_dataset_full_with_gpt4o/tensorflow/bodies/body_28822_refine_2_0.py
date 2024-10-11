import numpy as np # pragma: no cover

script_ops = type('Mock', (object,), {'py_func': lambda fn, inp, Tout: tf.py_function(func=fn, inp=inp, Tout=Tout)}) # pragma: no cover

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
