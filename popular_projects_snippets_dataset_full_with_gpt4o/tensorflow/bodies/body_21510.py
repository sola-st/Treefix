# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
save_path = os.path.join(self.get_temp_dir(), "sharded_basics")

# Build a graph with 2 parameter nodes on different devices.
with session.Session(
    target="",
    config=config_pb2.ConfigProto(device_count={"CPU": 2})) as sess:
    with sess.graph.device("/cpu:0"):
        v0 = variables.VariableV1(10, name="v0")
        t0 = saver_test_utils.CheckpointedOp(name="t0")
    with sess.graph.device("/cpu:1"):
        v1 = variables.VariableV1(20, name="v1")
        t1 = saver_test_utils.CheckpointedOp(name="t1")
    save = saver_module.Saver(
        {
            "v0": v0,
            "v1": v1,
            "t0": t0.saveable,
            "t1": t1.saveable
        },
        write_version=self._WRITE_VERSION,
        sharded=True)
    self.evaluate(variables.global_variables_initializer())
    t0.insert("k1", 30.0).run()
    t1.insert("k2", 40.0).run()
    val = save.save(sess, save_path)
    if save._write_version is saver_pb2.SaverDef.V1:
        self.assertEqual(save_path + "-?????-of-00002", val)
    else:
        self.assertEqual(save_path, val)
    meta_graph_filename = checkpoint_management.meta_graph_filename(val)
    self.assertEqual(save_path + ".meta", meta_graph_filename)

if save._write_version is saver_pb2.SaverDef.V1:
    # Restore different ops from shard 0 of the saved files.
    with session.Session(
        target="",
        config=config_pb2.ConfigProto(device_count={"CPU": 2})) as sess:
        with sess.graph.device("/cpu:0"):
            v0 = variables.VariableV1(111, name="v0")
            t0 = saver_test_utils.CheckpointedOp(name="t0")
        save = saver_module.Saver(
            {
                "v0": v0,
                "t0": t0.saveable
            },
            write_version=self._WRITE_VERSION,
            sharded=True)
        self.evaluate(variables.global_variables_initializer())
        t0.insert("k11", 33.0).run()
        self.assertEqual(111, self.evaluate(v0))
        self.assertEqual(b"k11", self.evaluate(t0.keys()))
        self.assertEqual(33.0, self.evaluate(t0.values()))
        save.restore(sess, save_path + "-00000-of-00002")
        self.assertEqual(10, self.evaluate(v0))
        self.assertEqual(b"k1", self.evaluate(t0.keys()))
        self.assertEqual(30.0, self.evaluate(t0.values()))

    # Restore different ops from shard 1 of the saved files.
    with session.Session(
        target="",
        config=config_pb2.ConfigProto(device_count={"CPU": 2})) as sess:
        with sess.graph.device("/cpu:0"):
            v1 = variables.VariableV1(222)
            t1 = saver_test_utils.CheckpointedOp(name="t1")
        save = saver_module.Saver(
            {
                "v1": v1,
                "t1": t1.saveable
            },
            write_version=self._WRITE_VERSION,
            sharded=True)
        self.evaluate(variables.global_variables_initializer())
        t1.insert("k22", 44.0).run()
        self.assertEqual(222, self.evaluate(v1))
        self.assertEqual(b"k22", self.evaluate(t1.keys()))
        self.assertEqual(44.0, self.evaluate(t1.values()))
        save.restore(sess, save_path + "-00001-of-00002")
        self.assertEqual(20, self.evaluate(v1))
        self.assertEqual(b"k2", self.evaluate(t1.keys()))
        self.assertEqual(40.0, self.evaluate(t1.values()))

    # Now try a restore with the sharded filename.
with session.Session(
    target="",
    config=config_pb2.ConfigProto(device_count={"CPU": 2})) as sess:
    with sess.graph.device("/cpu:0"):
        v0 = variables.VariableV1(111, name="v0")
        t0 = saver_test_utils.CheckpointedOp(name="t0")
    with sess.graph.device("/cpu:1"):
        v1 = variables.VariableV1(222, name="v1")
        t1 = saver_test_utils.CheckpointedOp(name="t1")
    save = saver_module.Saver(
        {
            "v0": v0,
            "v1": v1,
            "t0": t0.saveable,
            "t1": t1.saveable
        },
        write_version=self._WRITE_VERSION,
        sharded=True)
    self.evaluate(variables.global_variables_initializer())
    t0.insert("k11", 33.0).run()
    t1.insert("k22", 44.0).run()
    self.assertEqual(111, self.evaluate(v0))
    self.assertEqual(222, self.evaluate(v1))
    self.assertEqual(b"k11", self.evaluate(t0.keys()))
    self.assertEqual(33.0, self.evaluate(t0.values()))
    self.assertEqual(b"k22", self.evaluate(t1.keys()))
    self.assertEqual(44.0, self.evaluate(t1.values()))
    save_path = os.path.join(self.get_temp_dir(), "sharded_basics")
    if save._write_version is saver_pb2.SaverDef.V1:
        save.restore(sess, save_path + "-?????-of-?????")
    else:
        save.restore(sess, save_path)
    self.assertEqual(10, self.evaluate(v0))
    self.assertEqual(20, self.evaluate(v1))
    self.assertEqual(b"k1", self.evaluate(t0.keys()))
    self.assertEqual(30.0, self.evaluate(t0.values()))
    self.assertEqual(b"k2", self.evaluate(t1.keys()))
    self.assertEqual(40.0, self.evaluate(t1.values()))

if save._write_version is saver_pb2.SaverDef.V1:
    self.assertEqual(
        checkpoint_management.latest_checkpoint(self.get_temp_dir()),
        os.path.join(self.get_temp_dir(), "sharded_basics-?????-of-00002"))
else:
    self.assertEqual(
        checkpoint_management.latest_checkpoint(self.get_temp_dir()),
        os.path.join(self.get_temp_dir(), "sharded_basics"))
