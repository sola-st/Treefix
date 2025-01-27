# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
lengths = _list_with_ellipsis_to_str(self.static_lengths())
exit(("<DynamicRaggedShape "
        "lengths=%s num_row_partitions=%r>" %
        (lengths, self.num_row_partitions)))
