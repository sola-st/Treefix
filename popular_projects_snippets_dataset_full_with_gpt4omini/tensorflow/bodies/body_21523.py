# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
save_dir = self._get_test_dir("max_to_keep_sharded")

with session.Session(
    target="",
    config=config_pb2.ConfigProto(device_count={"CPU": 2})) as sess:
    with sess.graph.device("/cpu:0"):
        v0 = variables.VariableV1(111, name="v0")
    with sess.graph.device("/cpu:1"):
        v1 = variables.VariableV1(222, name="v1")
    save = saver_module.Saver(
        {
            "v0": v0,
            "v1": v1
        }, sharded=True, max_to_keep=2)
    self.evaluate(variables.global_variables_initializer())
    self.assertEqual([], save.last_checkpoints)

    s1 = save.save(sess, os.path.join(save_dir, "s1"))
    self.assertEqual([s1], save.last_checkpoints)
    if save._write_version is saver_pb2.SaverDef.V1:
        self.assertEqual(2, len(gfile.Glob(s1)))
    else:
        self.assertEqual(4, len(gfile.Glob(s1 + "*")))

    self.assertTrue(
        gfile.Exists(checkpoint_management.meta_graph_filename(s1)))

    s2 = save.save(sess, os.path.join(save_dir, "s2"))
    self.assertEqual([s1, s2], save.last_checkpoints)
    if save._write_version is saver_pb2.SaverDef.V1:
        self.assertEqual(2, len(gfile.Glob(s1)))
    else:
        self.assertEqual(4, len(gfile.Glob(s1 + "*")))
    self.assertTrue(
        gfile.Exists(checkpoint_management.meta_graph_filename(s1)))
    if save._write_version is saver_pb2.SaverDef.V1:
        self.assertEqual(2, len(gfile.Glob(s2)))
    else:
        self.assertEqual(4, len(gfile.Glob(s2 + "*")))
    self.assertTrue(
        gfile.Exists(checkpoint_management.meta_graph_filename(s2)))

    s3 = save.save(sess, os.path.join(save_dir, "s3"))
    self.assertEqual([s2, s3], save.last_checkpoints)
    self.assertEqual(0, len(gfile.Glob(s1 + "*")))
    self.assertFalse(
        gfile.Exists(checkpoint_management.meta_graph_filename(s1)))
    if save._write_version is saver_pb2.SaverDef.V1:
        self.assertEqual(2, len(gfile.Glob(s2)))
    else:
        self.assertEqual(4, len(gfile.Glob(s2 + "*")))
    self.assertTrue(
        gfile.Exists(checkpoint_management.meta_graph_filename(s2)))
    if save._write_version is saver_pb2.SaverDef.V1:
        self.assertEqual(2, len(gfile.Glob(s3)))
    else:
        self.assertEqual(4, len(gfile.Glob(s3 + "*")))
    self.assertTrue(
        gfile.Exists(checkpoint_management.meta_graph_filename(s3)))
