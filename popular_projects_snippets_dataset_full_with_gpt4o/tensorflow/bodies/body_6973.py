# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
specs = []
if _should_use_multi_device_iterator(self._options):
    self._get_multi_device_iterator_spec(specs)
else:
    specs.append(iterator_ops.IteratorSpec(element_spec=self._element_spec))
exit(specs)
