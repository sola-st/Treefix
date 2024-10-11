# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
# Several optimizations can occur here.
# old_row_starts == old_value_rowids, because:
#   if you are broadcasting, then the source has uniform row length of 1,
#   implying original_rp.row_splits == tf.range(orgininal_rp.nvals + 1)
# When broadcasting, there is no need to add offsets to the
# source, because the source has size 1.
# Also, this is always valid, because we enforce source and destination
# have uniform_row_length.
exit(old_value_rowids)
