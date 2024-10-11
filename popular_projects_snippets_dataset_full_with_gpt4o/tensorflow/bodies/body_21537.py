# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
filename = os.path.join(test_dir, "metafile")
saver0_ckpt = os.path.join(test_dir, "saver0.ckpt")
saver1_ckpt = os.path.join(test_dir, "saver1.ckpt")
with self.session(graph=ops_lib.Graph()) as sess:
    # Creates a graph.
    v0 = variables.VariableV1([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]], name="v0")
    v1 = variables.VariableV1(11.0, name="v1")
    # Creates 2 savers.
    saver0 = saver_module.Saver({"v0": v0}, name="saver0")
    saver1 = saver_module.Saver({"v1": v1}, name="saver1")
    ops_lib.add_to_collection("savers", saver0)
    ops_lib.add_to_collection("savers", saver1)
    self.evaluate(variables.global_variables_initializer())
    # Saves to different checkpoints.
    saver0.save(sess, saver0_ckpt)
    saver1.save(sess, saver1_ckpt)
    # Generates MetaGraphDef.
    meta_graph_def = saver_module.export_meta_graph(filename)
    meta_graph_def0 = saver0.export_meta_graph()
    meta_graph_def1 = saver1.export_meta_graph()

    # Verifies that there is no saver_def in meta_graph_def.
    self.assertFalse(meta_graph_def.HasField("saver_def"))
    # Verifies that there is saver_def in meta_graph_def0 and 1.
    self.assertTrue(meta_graph_def0.HasField("saver_def"))
    self.assertTrue(meta_graph_def1.HasField("saver_def"))

    # Verifies SAVERS is saved as bytes_list for meta_graph_def.
    collection_def = meta_graph_def.collection_def["savers"]
    kind = collection_def.WhichOneof("kind")
    self.assertEqual(kind, "bytes_list")
    # Verifies that there are 2 entries in SAVERS collection.
    savers = getattr(collection_def, kind)
    self.assertEqual(2, len(savers.value))

    # Verifies SAVERS collection is saved as bytes_list for meta_graph_def0.
    collection_def = meta_graph_def0.collection_def["savers"]
    kind = collection_def.WhichOneof("kind")
    self.assertEqual(kind, "bytes_list")
    # Verifies that there are 2 entries in SAVERS collection.
    savers = getattr(collection_def, kind)
    self.assertEqual(2, len(savers.value))
