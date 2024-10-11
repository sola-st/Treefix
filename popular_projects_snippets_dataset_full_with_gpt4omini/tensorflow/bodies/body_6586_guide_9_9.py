input_type = 'tf.data.Dataset' # pragma: no cover
api_type = 'test_api' # pragma: no cover
iteration_type = 'single_iteration' # pragma: no cover
enable_get_next_as_optional = True # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self._create_dataset_or_input_fn = lambda input_type, dataset_fn: dataset_fn(None) # pragma: no cover
self._test_input_iteration = lambda input_type, api_type, iteration_type, dataset_fn, worker_device_pairs, expected_values, distribution: print('Test executed with expected values:', expected_values) # pragma: no cover
worker_device_pairs = [('/device:CPU:0', ['/device:GPU:0', '/device:GPU:1'])] # pragma: no cover
distribution = type('Mock', (object,), {'extended': type('MockExtended', (object,), {'experimental_enable_get_next_as_optional': enable_get_next_as_optional})()})() # pragma: no cover
expected_values = [[(i, i**2), (i + 1, (i + 1)**2)] for i in range(0, 10, 2)] # pragma: no cover

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
