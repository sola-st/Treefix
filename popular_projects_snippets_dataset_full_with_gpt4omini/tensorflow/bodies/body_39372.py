# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/save_util_v1_test.py
root = autotrackable.AutoTrackable()
root.v = variables.Variable(1.0)
root.registered = TrackableWithRegisteredSaver()
named_saveable_objects, _, _, registered_savers = (
    save_util_v1.serialize_gathered_objects(
        graph_view.ObjectGraphView(root)))

self.assertLen(named_saveable_objects, 1)
self.assertIs(named_saveable_objects[0].op, root.v)
self.assertDictEqual(
    {"Custom.RegisteredSaver": {"registered": root.registered}},
    registered_savers)
