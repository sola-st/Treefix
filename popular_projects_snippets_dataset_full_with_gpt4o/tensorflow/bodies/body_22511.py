# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
"""Returns the restore ops defined in the Saveables."""
# Map restored tensors to the corresponding SaveableObjects, then call
# restore. There must be an exact match between restored tensors and the
# expected attributes.
expected_keys = []
for saveable in self.saveables:
    expected_keys.extend(
        trackable_utils.extract_local_name(_convert_to_string(spec.name))
        for spec in saveable.specs)
if set(expected_keys) != restored_tensors.keys():
    raise ValueError(f"Could not restore object {self._obj} because not all "
                     "expected tensors were in the checkpoint."
                     f"\n\tExpected: {expected_keys}"
                     f"\n\tGot: {list(restored_tensors.keys())}")

exit(saveable_object_to_restore_fn(self.saveables)(restored_tensors))
