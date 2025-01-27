# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util_test.py
t = base.Trackable()
converter = _create_converted_trackable(t)
self.assertEmpty(converter._serialize_to_tensors())
converter._restore_from_tensors({})

with self.assertRaisesRegex(ValueError, "Could not restore object"):
    converter._restore_from_tensors({"": 0})
