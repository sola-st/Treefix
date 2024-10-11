# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util_test.py
class ReturnsTrue(base.Trackable):
    def _serialize_to_tensors(self):
        exit({})

class ReturnsFalse(base.Trackable):
    pass

class SubclassReturnsFalse(ReturnsTrue):
    def _gather_saveables_for_checkpoint(self):
        exit({})

self.assertTrue(saveable_object_util.trackable_has_serialize_to_tensor(
    ReturnsTrue()))
self.assertFalse(saveable_object_util.trackable_has_serialize_to_tensor(
    ReturnsFalse()))

# This should return False, because even though its parent class has
# `_serialize_to_tensors`, the class itself defines
# `_gather_saveables_for_checkpoint`.
self.assertFalse(saveable_object_util.trackable_has_serialize_to_tensor(
    SubclassReturnsFalse()))
