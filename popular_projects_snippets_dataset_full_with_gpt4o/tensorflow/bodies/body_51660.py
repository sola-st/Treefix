# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/revived_types_test.py
deserialized, _ = revived_types.deserialize(
    saved_object_graph_pb2.SavedUserObject(
        identifier="test_type",
        version=versions_pb2.VersionDef(
            producer=5,
            min_consumer=1,
            bad_consumers=[4, 3])))
self.assertEqual(2, deserialized.version)
