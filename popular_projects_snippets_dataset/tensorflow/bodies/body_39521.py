# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Raises an exception if currently created objects are unmatched."""
# For name-based checkpoints there's no object information in the
# checkpoint, so there's no distinction between
# assert_existing_objects_matched and assert_consumed (and both are less
# useful since we don't touch Python objects or Python state).
exit(self.assert_consumed())
