input_type = 'mock_input_type' # pragma: no cover
api_type = 'mock_api_type' # pragma: no cover
iteration_type = 'mock_iteration_type' # pragma: no cover
enable_get_next_as_optional = True # pragma: no cover
class MockExtendedDistribution: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.experimental_enable_get_next_as_optional = None # pragma: no cover
 # pragma: no cover
class MockDistribution: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.extended = MockExtendedDistribution() # pragma: no cover
 # pragma: no cover
distribution = MockDistribution() # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def _create_dataset_or_input_fn(self, input_type, dataset_fn): # pragma: no cover
        return dataset_fn # pragma: no cover
 # pragma: no cover
    def _test_input_iteration(self, input_type, api_type, iteration_type, dataset_or_input_fn, worker_device_pairs, expected_values, distribution): # pragma: no cover
        dataset = dataset_or_input_fn(None) # pragma: no cover
        iterator = iter(dataset) # pragma: no cover
        actual = [next(iterator) for _ in range(10)] # pragma: no cover
        result = [(item[0].numpy(), item[1].numpy()) for item in actual] # pragma: no cover
        print(f'Expected: {expected_values}, Actual: {result}') # pragma: no cover
        flat_expected = [item for sublist in expected_values for item in sublist] # pragma: no cover
        assert result == flat_expected, f'Expected {flat_expected}, but got {result}' # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
from l3.Runtime import _l_
worker_device_pairs = [("/device:CPU:0", ["/device:GPU:0",
                                          "/device:GPU:1"])]
_l_(21719)

def dataset_fn(ctx):
    _l_(21724)

    del ctx
    _l_(21720)
    dataset1 = dataset_ops.Dataset.range(10)
    _l_(21721)
    dataset2 = dataset_ops.Dataset.range(10).map(lambda x: x**2)
    _l_(21722)
    aux = dataset_ops.Dataset.zip((dataset1, dataset2))
    _l_(21723)
    exit(aux)

dataset_or_input_fn = self._create_dataset_or_input_fn(
    input_type, dataset_fn)
_l_(21725)

expected_values = [
    [(i, i**2), (i + 1, (i + 1)**2)] for i in range(0, 10, 2)
]
_l_(21726)

distribution.extended.experimental_enable_get_next_as_optional = (
    enable_get_next_as_optional)
_l_(21727)

# Input_context is not passed in and thus no sharding.
self._test_input_iteration(input_type, api_type, iteration_type,
                           dataset_or_input_fn, worker_device_pairs,
                           expected_values, distribution)
_l_(21728)
