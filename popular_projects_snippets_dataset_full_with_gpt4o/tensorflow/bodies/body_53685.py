# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Compares MetaGraphDefs `a` and `b` in unit test class `tester`."""
# Carefully check the collection_defs
tester.assertEqual(set(a.collection_def), set(b.collection_def))
collection_keys = a.collection_def.keys()
for k in collection_keys:
    a_value = a.collection_def[k]
    b_value = b.collection_def[k]
    proto_type = ops.get_collection_proto_type(k)
    if proto_type:
        a_proto = proto_type()
        b_proto = proto_type()
        # Number of entries in the collections is the same
        tester.assertEqual(
            len(a_value.bytes_list.value), len(b_value.bytes_list.value))
        for (a_value_item, b_value_item) in zip(a_value.bytes_list.value,
                                                b_value.bytes_list.value):
            a_proto.ParseFromString(a_value_item)
            b_proto.ParseFromString(b_value_item)
            tester.assertProtoEquals(a_proto, b_proto)
    else:
        tester.assertEquals(a_value, b_value)
  # Compared the fields directly, remove their raw values from the
  # proto comparison below.
a.ClearField("collection_def")
b.ClearField("collection_def")

# Check the graph_defs.
assert_equal_graph_def(a.graph_def, b.graph_def, checkpoint_v2=True)
# Check graph_def versions (ignored by assert_equal_graph_def).
tester.assertProtoEquals(a.graph_def.versions, b.graph_def.versions)
# Compared the fields directly, remove their raw values from the
# proto comparison below.
a.ClearField("graph_def")
b.ClearField("graph_def")

tester.assertProtoEquals(a, b)
