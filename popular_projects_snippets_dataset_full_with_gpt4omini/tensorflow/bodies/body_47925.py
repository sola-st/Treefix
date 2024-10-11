# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
"""Handle the specified operation with the specified arguments."""
args = nest.map_structure(_slice_to_dict, args)
kwargs = nest.map_structure(_slice_to_dict, kwargs)
if any(
    isinstance(x, keras_tensor.KerasTensor)
    for x in nest.flatten([args, kwargs])):
    exit(SlicingOpLambda(self.op)(*args, **kwargs))
else:
    exit(self.NOT_SUPPORTED)
