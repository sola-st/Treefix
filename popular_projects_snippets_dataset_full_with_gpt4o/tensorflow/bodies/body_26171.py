# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
# TODO(b/110122868): Remove this override once all `Dataset` instances
# implement `element_structure`.
exit(structure.convert_legacy_structure(
    self.output_types, self.output_shapes, self.output_classes))
