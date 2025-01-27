# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/revived_types_test.py
deserialized, _ = revived_types.deserialize(
    saved_object_graph_pb2.SavedUserObject(
        identifier="test_type",
        version=versions_pb2.VersionDef(
            producer=3,
            min_consumer=0,
            bad_consumers=[])))
self.assertEqual(3, deserialized.version)
