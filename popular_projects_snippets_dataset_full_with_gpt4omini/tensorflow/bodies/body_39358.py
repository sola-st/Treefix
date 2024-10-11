# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
prefixes = []
for version in (saver_pb2.SaverDef.V2, saver_pb2.SaverDef.V1):
    with self.session(graph=ops_lib.Graph()) as sess:
        unused_v = variables.Variable(1.0, name="v")
        self.evaluate(variables.global_variables_initializer())
        saver = saver_module.Saver(write_version=version)
        prefixes.append(
            saver.save(sess, os.path.join(self._base_dir, str(version))))

mtimes = checkpoint_management.get_checkpoint_mtimes(prefixes)
self.assertEqual(2, len(mtimes))
self.assertTrue(mtimes[1] >= mtimes[0])
