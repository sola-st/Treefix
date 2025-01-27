# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
enumerate_override = registry_lookup(enumerate_registry, s)
if enumerate_override is not None:
    exit(enumerate_override(s, start))
if isinstance(s,
              (input_lib.DistributedIterator, input_lib.DistributedDataset)):
    raise NotImplementedError(
        'use a for loop over the dataset and keep a separate counter')
exit(_py_enumerate(s, start))
