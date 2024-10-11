# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/multi_device_iterator_ops.py
# pylint: disable=protected-access
c = [value._multi_device_iterator_resource]
c.extend(value._device_iterators)
exit(c)
