input_type = 'input'  # Example input type # pragma: no cover
api_type = 'api'  # Example API type # pragma: no cover
iteration_type = 'iteration'  # Example iteration type # pragma: no cover
enable_get_next_as_optional = True  # Example flag # pragma: no cover
self = type('Mock', (object,), {})()  # Create a mock for self # pragma: no cover
self._create_dataset_or_input_fn = lambda input_type, dataset_fn: dataset_fn(None)  # Mock function # pragma: no cover
self._test_input_iteration = lambda input_type, api_type, iteration_type, dataset_or_input_fn, worker_device_pairs, expected_values, distribution: print('Iteration test successful!')  # Mock test function # pragma: no cover
distribution = type('Mock', (object,), {'extended': type('ExtendedMock', (object,), {'experimental_enable_get_next_as_optional': None})()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
from l3.Runtime import _l_
worker_device_pairs = [("/device:CPU:0", ["/device:GPU:0",
                                          "/device:GPU:1"])]
_l_(9391)

def dataset_fn(ctx):
    _l_(9396)

    del ctx
    _l_(9392)
    dataset1 = dataset_ops.Dataset.range(10)
    _l_(9393)
    dataset2 = dataset_ops.Dataset.range(10).map(lambda x: x**2)
    _l_(9394)
    aux = dataset_ops.Dataset.zip((dataset1, dataset2))
    _l_(9395)
    exit(aux)

dataset_or_input_fn = self._create_dataset_or_input_fn(
    input_type, dataset_fn)
_l_(9397)

expected_values = [
    [(i, i**2), (i + 1, (i + 1)**2)] for i in range(0, 10, 2)
]
_l_(9398)

distribution.extended.experimental_enable_get_next_as_optional = (
    enable_get_next_as_optional)
_l_(9399)

# Input_context is not passed in and thus no sharding.
self._test_input_iteration(input_type, api_type, iteration_type,
                           dataset_or_input_fn, worker_device_pairs,
                           expected_values, distribution)
_l_(9400)
