# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/multi_device_iterator_test.py
dataset = from_generator_op._GeneratorDataset(
    1,
    init_fn,
    next_fn,
    finalize_fn,
    output_signature=tensor_spec.TensorSpec([], dtypes.int64))
iterator = multi_device_iterator_ops.OwnedMultiDeviceIterator(
    dataset, [self._devices[1], self._devices[2]])
next(iterator)
