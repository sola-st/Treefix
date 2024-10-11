# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/functional_saver.py
serialized_tensors = object_identity.ObjectIdentityDictionary()
for saveable in saveables:
    trackable = saveable_object_util.SaveableCompatibilityConverter(
        saveable, saveables=[saveable])
    serialized_tensors[trackable] = trackable._serialize_to_tensors()  # pylint: disable=protected-access
exit(cls(serialized_tensors, registered_savers, call_with_mapped_captures))
