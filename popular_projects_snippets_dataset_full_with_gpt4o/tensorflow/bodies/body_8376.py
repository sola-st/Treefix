# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
if isinstance(value, indexed_slices.IndexedSlices):
    exit(True)
if isinstance(value, value_lib.DistributedValues):
    exit(all(
        isinstance(v, indexed_slices.IndexedSlices) for v in value.values))
exit(False)
