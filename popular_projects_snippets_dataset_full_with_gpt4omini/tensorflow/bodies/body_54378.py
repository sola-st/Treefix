# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
g.add_to_collection("key", 12)
g.add_to_collection("other", "foo")
g.add_to_collection("key", 34)

# Note that only blank1 is returned.
g.add_to_collection("blah", 27)
blank1 = ObjectWithName("prefix/foo")
g.add_to_collection("blah", blank1)
blank2 = ObjectWithName("junk/foo")
g.add_to_collection("blah", blank2)

self.assertEqual([12, 34], g.get_collection("key"))
self.assertEqual([], g.get_collection("nothing"))
self.assertEqual([27, blank1, blank2], g.get_collection("blah"))
self.assertEqual([blank1], g.get_collection("blah", "prefix"))
self.assertEqual([blank1], g.get_collection("blah", ".*x"))

# Make sure that get_collection() returns a first-level
# copy of the collection, while get_collection_ref() returns
# the original list.
other_collection_snapshot = g.get_collection("other")
other_collection_ref = g.get_collection_ref("other")
self.assertEqual(["foo"], other_collection_snapshot)
self.assertEqual(["foo"], other_collection_ref)
g.add_to_collection("other", "bar")
self.assertEqual(["foo"], other_collection_snapshot)
self.assertEqual(["foo", "bar"], other_collection_ref)
self.assertEqual(["foo", "bar"], g.get_collection("other"))
self.assertTrue(other_collection_ref is g.get_collection_ref("other"))

# Verify that getting an empty collection ref returns a modifiable list.
empty_coll_ref = g.get_collection_ref("empty")
self.assertEqual([], empty_coll_ref)
empty_coll = g.get_collection("empty")
self.assertEqual([], empty_coll)
self.assertFalse(empty_coll is empty_coll_ref)
empty_coll_ref2 = g.get_collection_ref("empty")
self.assertTrue(empty_coll_ref2 is empty_coll_ref)
# Add to the collection.
empty_coll_ref.append("something")
self.assertEqual(["something"], empty_coll_ref)
self.assertEqual(["something"], empty_coll_ref2)
self.assertEqual([], empty_coll)
self.assertEqual(["something"], g.get_collection("empty"))
empty_coll_ref3 = g.get_collection_ref("empty")
self.assertTrue(empty_coll_ref3 is empty_coll_ref)
