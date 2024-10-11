# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/save_util_v1_test.py
root = autotrackable.AutoTrackable()
root.v = variables.Variable(1.0)
root.registered = TrackableWithRegisteredSaver()

copy_of_registered = TrackableWithRegisteredSaver()
copy_of_v = variables.Variable(1.0)
object_map = object_identity.ObjectIdentityDictionary()
object_map[root.registered] = copy_of_registered
object_map[root.v] = copy_of_v

named_saveable_objects, _, _, registered_savers = (
    save_util_v1.serialize_gathered_objects(
        graph_view.ObjectGraphView(root), object_map))

self.assertLen(named_saveable_objects, 1)
self.assertIsNot(named_saveable_objects[0].op, root.v)
self.assertIs(named_saveable_objects[0].op, copy_of_v)

ret_value = registered_savers["Custom.RegisteredSaver"]["registered"]
self.assertIsNot(root.registered, ret_value)
self.assertIs(copy_of_registered, ret_value)
