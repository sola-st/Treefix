# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
with self.cached_session():
    # Creates a graph.
    v0 = variables.VariableV1(10.0, name="v0")
    # Creates a saver.
    save = saver_module.Saver({"v0": v0})
    # Generates MetaGraphDef.
    meta_graph_def = meta_graph_pb2.MetaGraphDef()

    # Verifies that collection with unsupported key will not be added.
    ops_lib.add_to_collection(save, 3)
    save._add_collection_def(meta_graph_def, save)
    self.assertEqual(len(meta_graph_def.collection_def), 0)

    # Verifies that collection where item type does not match expected
    # type will not be added.
    ops_lib.add_to_collection("int_collection", 3)
    ops_lib.add_to_collection("int_collection", 3.5)
    save._add_collection_def(meta_graph_def, "int_collection")
    self.assertEqual(len(meta_graph_def.collection_def), 0)
