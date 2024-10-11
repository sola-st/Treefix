# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
filename = os.path.join(test_dir, "metafile")
saver0_ckpt = os.path.join(test_dir, "saver0.ckpt")
saver1_ckpt = os.path.join(test_dir, "saver1.ckpt")
with self.session(graph=ops_lib.Graph()) as sess:
    # Imports from meta_graph.
    saver_module.import_meta_graph(filename)
    # Retrieves SAVERS collection. Verifies there are 2 entries.
    savers = ops_lib.get_collection("savers")
    self.assertEqual(2, len(savers))
    # Retrieves saver0. Verifies that new_saver0 can restore v0, but not v1.
    new_saver0 = savers[0]
    new_saver0.restore(sess, saver0_ckpt)
    v0 = sess.graph.get_tensor_by_name("v0:0")
    v1 = sess.graph.get_tensor_by_name("v1:0")
    self.assertAllEqual([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]],
                        self.evaluate(v0))
    self.assertEqual([3, 2], v0.get_shape())
    self.assertEqual([], v1.get_shape())
    with self.assertRaisesWithPredicateMatch(
        errors_impl.OpError, lambda e: "uninitialized value v1" in e.message):
        self.evaluate(v1)
    # Retrieves saver1. Verifies that new_saver1 can restore v1.
    new_saver1 = savers[1]
    new_saver1.restore(sess, saver1_ckpt)
    v1 = sess.graph.get_tensor_by_name("v1:0")
    self.assertEqual(11.0, self.evaluate(v1))
