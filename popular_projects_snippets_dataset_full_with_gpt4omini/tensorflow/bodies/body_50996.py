# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("custom_saveable")
builder = saved_model_builder._SavedModelBuilder(export_dir)

with session.Session(
    graph=ops.Graph(),
    config=config_pb2.ConfigProto(device_count={"CPU": 2})) as sess:
    # CheckpointedOp is a key-value table that can be saved across sessions.
    # The table register itself in SAVEABLE_OBJECTS collection.
    v1 = saver_test_utils.CheckpointedOp(name="v1")
    self.evaluate(variables.global_variables_initializer())
    v1.insert("k1", 3.0).run()
    # Once the table is restored, we can access it through this reference.
    ops.add_to_collection("table_ref", v1.table_ref)
    builder.add_meta_graph_and_variables(sess, ["foo"])

# Save the SavedModel to disk.
builder.save()

with session.Session(
    graph=ops.Graph(),
    config=config_pb2.ConfigProto(device_count={"CPU": 2})) as sess:
    loader.load(sess, ["foo"], export_dir)
    # Instantiate a wrapper object from the checkpointed reference.
    v1 = saver_test_utils.CheckpointedOp(
        name="v1", table_ref=ops.get_collection("table_ref")[0])
    self.assertEqual(b"k1", v1.keys().eval())
    self.assertEqual(3.0, v1.values().eval())
