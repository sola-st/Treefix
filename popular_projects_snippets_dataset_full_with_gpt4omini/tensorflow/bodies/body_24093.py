# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/dumping_wrapper_test.py
sess = dumping_wrapper.DumpingDebugWrapperSession(
    self.sess, session_root=self.session_root, log_usage=False)
sess.run(self.inc_v)

dump_dirs = glob.glob(os.path.join(self.session_root, "run_*"))
self.assertEqual(1, len(dump_dirs))

self._assert_correct_run_subdir_naming(os.path.basename(dump_dirs[0]))
dump = debug_data.DebugDumpDir(dump_dirs[0])
self.assertAllClose([10.0], dump.get_tensors("v", 0, "DebugIdentity"))

self.assertEqual(repr(self.inc_v), dump.run_fetches_info)
self.assertEqual(repr(None), dump.run_feed_keys_info)
