input_type = 'dummy_input_type' # pragma: no cover
api_type = 'dummy_api_type' # pragma: no cover
iteration_type = 'dummy_iteration_type' # pragma: no cover
enable_get_next_as_optional = True # pragma: no cover
distribution = type('MockDistribution', (object,), { # pragma: no cover
    'extended': type('MockExtended', (object,), { # pragma: no cover
        'experimental_enable_get_next_as_optional': None # pragma: no cover
    })() # pragma: no cover
})() # pragma: no cover
class MockSelf: # pragma: no cover
    def _create_dataset_or_input_fn(self, input_type, dataset_fn): # pragma: no cover
        def wrapper_fn(ctx): # pragma: no cover
            return dataset_fn(ctx) # pragma: no cover
        return wrapper_fn # pragma: no cover
 # pragma: no cover
    def _test_input_iteration(self, input_type, api_type, iteration_type, dataset_or_input_fn, worker_device_pairs, expected_values, distribution): # pragma: no cover
        dataset = dataset_or_input_fn(None) # pragma: no cover
        iterator = iter(dataset) # pragma: no cover
        result = [] # pragma: no cover
        while True: # pragma: no cover
            try: # pragma: no cover
                result.append(next(iterator).numpy()) # pragma: no cover
            except StopIteration: # pragma: no cover
                break # pragma: no cover
        print('Result:', result) # pragma: no cover
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
