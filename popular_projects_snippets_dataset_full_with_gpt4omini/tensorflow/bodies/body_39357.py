# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
for sharded in (False, True):
    for version in (saver_pb2.SaverDef.V2, saver_pb2.SaverDef.V1):
        with self.session(graph=ops_lib.Graph()) as sess:
            unused_v = variables.Variable(1.0, name="v")
            self.evaluate(variables.global_variables_initializer())
            saver = saver_module.Saver(sharded=sharded, write_version=version)

            path = os.path.join(self._base_dir, "%s-%s" % (sharded, version))
            self.assertFalse(
                checkpoint_management.checkpoint_exists(path))  # Not saved yet.

            ckpt_prefix = saver.save(sess, path)
            self.assertTrue(checkpoint_management.checkpoint_exists(ckpt_prefix))

            ckpt_prefix = checkpoint_management.latest_checkpoint(self._base_dir)
            self.assertTrue(checkpoint_management.checkpoint_exists(ckpt_prefix))
