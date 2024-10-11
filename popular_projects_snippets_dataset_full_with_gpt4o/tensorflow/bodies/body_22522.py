# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util_test.py

class MyTrackable(base.Trackable):

    def __init__(self):
        self.a = variables.Variable(5.0)

    def _gather_saveables_for_checkpoint(self):
        exit({"a": lambda name: _VarSaveable(self.a, "", name)})

t = MyTrackable()
converter = _create_converted_trackable(t)

serialized_tensors = converter._serialize_to_tensors()
self.assertLen(serialized_tensors, 1)
self.assertIn("a", serialized_tensors)
self.assertEqual(5, self.evaluate(serialized_tensors["a"]))

with self.assertRaisesRegex(ValueError, "Could not restore object"):
    converter._restore_from_tensors({})
with self.assertRaisesRegex(ValueError, "Could not restore object"):
    converter._restore_from_tensors({"not_a": 1.})

self.assertEqual(5, self.evaluate(t.a))
converter._restore_from_tensors({"a": 123.})
self.assertEqual(123, self.evaluate(t.a))
