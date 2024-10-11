dataset_ops = type('Mock', (object,), {'Dataset': type('Mock', (object,), {'from_tensors': lambda x: 'dataset'})}) # pragma: no cover
scan_ops = type('Mock', (object,), {'scan': lambda initial_state, fn: 'scanned_dataset'}) # pragma: no cover
var = 5 # pragma: no cover

class MockDataset:  # Define the mock dataset class # pragma: no cover
    def __init__(self, tensors):  # Constructor that stores tensors # pragma: no cover
        self.tensors = tensors  # Store the input tensors # pragma: no cover
    @staticmethod # pragma: no cover
    def from_tensors(tensor):  # Static method to initialize from tensors # pragma: no cover
        return MockDataset(tensor)  # Return an instance of the mock class # pragma: no cover
    def apply(self, transformation):  # Apply method to handle dataset transformations # pragma: no cover
        return transformation(self)  # Apply the transformation # pragma: no cover
class MockScanOps:  # Define the mock scan operations class # pragma: no cover
    @staticmethod # pragma: no cover
    def scan(initial_state, fn):  # Static method for scanning # pragma: no cover
        def transformation(dataset):  # Define the transformation # pragma: no cover
            state = initial_state  # Initialize state # pragma: no cover
            for elem in dataset.tensors:  # Iterate through elements in the dataset # pragma: no cover
                state, new_elem = fn(state, elem)  # Apply the scan function # pragma: no cover
                yield new_elem  # Yield the resulting element # pragma: no cover
        return transformation # pragma: no cover
dataset_ops = type('Mock', (object,), {'Dataset': MockDataset}) # pragma: no cover
scan_ops = MockScanOps # pragma: no cover
var = 3 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/optimization_test.py
from l3.Runtime import _l_
aux = dataset_ops.Dataset.from_tensors(0).apply(
    scan_ops.scan(
        0, lambda old_state, elem: (old_state + 1, elem + old_state + var)))
_l_(20875)
exit(aux)
