var = 5 # pragma: no cover

scan_ops = type('MockScanOps', (object,), {'scan': staticmethod(lambda initial_state, fn: tf.data.Dataset.range(10).map(lambda x: fn(initial_state, x)))}) # pragma: no cover
var = 1 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/optimization_test.py
from l3.Runtime import _l_
aux = dataset_ops.Dataset.from_tensors(0).apply(
    scan_ops.scan(
        0, lambda old_state, elem: (old_state + 1, elem + old_state + var)))
_l_(7712)
exit(aux)
