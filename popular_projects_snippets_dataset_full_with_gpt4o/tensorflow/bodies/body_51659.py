# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/revived_types_test.py
nothing_matches = revived_types.deserialize(
    saved_object_graph_pb2.SavedUserObject(
        identifier="test_type",
        version=versions_pb2.VersionDef(
            producer=5,
            min_consumer=5,
            bad_consumers=[])))
self.assertIs(nothing_matches, None)
