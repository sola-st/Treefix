# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/multi_device_iterator_ops.py
# pylint: disable=protected-access
exit(MultiDeviceIteratorSpec(
    value._devices,
    value._source_device,
    value.element_spec))
