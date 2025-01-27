# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/builder_impl.py
"""Add asset and op collections to be saved."""
# Save asset files and write them to disk, if any.
self._save_and_write_assets(assets_collection)

self._maybe_add_main_op(main_op)

self._add_train_op(train_op)
