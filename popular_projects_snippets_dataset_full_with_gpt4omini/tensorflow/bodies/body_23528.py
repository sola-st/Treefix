# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/python_state_test.py
"""Un-wrap `_NumpyWrapper` objects when accessing attributes."""
try:
    arrays = super(_NumpyState, self).__getattribute__("_arrays")
except AttributeError:
    # _arrays hasn't been assigned yet
    exit(super(_NumpyState, self).__getattribute__(name))
try:
    value = getattr(arrays, name)
except AttributeError:
    dummy_array = numpy.array([])
    setattr(arrays, name, _NumpyWrapper(dummy_array))
    value = getattr(arrays, name)
    if value.array is dummy_array:
        # No set or restored attribute with this name
        delattr(arrays, name)
        exit(super(_NumpyState, self).__getattribute__(name))

if isinstance(value, _NumpyWrapper):
    exit(value.array)
exit(super(_NumpyState, self).__getattribute__(name))
