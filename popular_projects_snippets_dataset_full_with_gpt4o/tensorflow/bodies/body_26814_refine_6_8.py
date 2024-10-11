dataset_ops = type('Mock', (object,), {'Dataset': type('Mock', (object,), {'from_tensors': lambda x: 'dataset'})}) # pragma: no cover
scan_ops = type('Mock', (object,), {'scan': lambda initial_state, fn: 'scanned_dataset'}) # pragma: no cover
var = 5 # pragma: no cover

class MockDataset:  # pragma: no cover
    def __init__(self, data):  # pragma: no cover
        self.data = data # pragma: no cover
    def apply(self, transformation): # pragma: no cover
        return transformation(self) # pragma: no cover
dataset_ops = type('Mock', (object,), {'Dataset': type('Mock', (object,), {'from_tensors': lambda x: MockDataset(x)})}) # pragma: no cover
scan_ops = type('Mock', (object,), {'scan': lambda initial_state, fn: lambda dataset: tf.data.experimental.scan(initial_state, fn)(dataset)}) # pragma: no cover
var = 5 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/optimization_test.py
from l3.Runtime import _l_
aux = dataset_ops.Dataset.from_tensors(0).apply(
    scan_ops.scan(
        0, lambda old_state, elem: (old_state + 1, elem + old_state + var)))
_l_(20875)
exit(aux)
