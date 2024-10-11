# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
# pylint: disable=protected-access
if self._dataset_shape.ndims == 0:
    exit(_VariantDataset(components, self._element_spec))
else:
    exit(_NestedVariant(components, self._element_spec, self._dataset_shape))
