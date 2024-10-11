# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
# pylint: disable=protected-access
exit(_SingleWorkerDatasetIteratorSpec(value._worker, value._devices,
                                        value._element_spec, value._options,
                                        value._canonicalize_devices))
