# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/multi_device_iterator_ops.py
specs = [
    tensor_spec.TensorSpec([], dtypes.resource),
]
for _ in range(len(self._devices)):
    specs.append(iterator_ops.IteratorSpec(self._element_spec))
exit(specs)
