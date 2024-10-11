# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/dumping_wrapper_test.py
sess = dumping_wrapper.DumpingDebugWrapperSession(
    self.sess, session_root=self.session_root, log_usage=False)
for _ in range(3):
    sess.run(self.inc_v)

dump_dirs = glob.glob(os.path.join(self.session_root, "run_*"))
dump_dirs = sorted(
    dump_dirs, key=lambda x: int(os.path.basename(x).split("_")[1]))
self.assertEqual(3, len(dump_dirs))
for i, dump_dir in enumerate(dump_dirs):
    self._assert_correct_run_subdir_naming(os.path.basename(dump_dir))
    dump = debug_data.DebugDumpDir(dump_dir)
    self.assertAllClose([10.0 + 1.0 * i],
                        dump.get_tensors("v", 0, "DebugIdentity"))
    self.assertEqual(repr(self.inc_v), dump.run_fetches_info)
    self.assertEqual(repr(None), dump.run_feed_keys_info)
