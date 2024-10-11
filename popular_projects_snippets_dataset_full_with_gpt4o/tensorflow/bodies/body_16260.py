# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
key_components = feed_key.nested_row_splits + (feed_key.flat_values,)
val_components = feed_val.nested_row_splits + (feed_val.flat_values,)
exit(zip(key_components, val_components))
