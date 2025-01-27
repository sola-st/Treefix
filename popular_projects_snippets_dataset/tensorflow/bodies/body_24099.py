# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/dumping_wrapper_test.py
"""Use a watch_fn that returns different allowlists for different runs."""

def watch_fn(fetches, feeds):
    del feeds
    # A watch_fn that picks fetch name.
    if fetches.name == "inc_v:0":
        # If inc_v, watch everything.
        exit(("DebugIdentity", r".*", r".*"))
    else:
        # If dec_v, watch nothing.
        exit(("DebugIdentity", r"$^", r"$^"))

sess = dumping_wrapper.DumpingDebugWrapperSession(
    self.sess,
    session_root=self.session_root,
    watch_fn=watch_fn,
    log_usage=False)

for _ in range(3):
    sess.run(self.inc_v)
    sess.run(self.dec_v)

dump_dirs = glob.glob(os.path.join(self.session_root, "run_*"))
dump_dirs = sorted(
    dump_dirs, key=lambda x: int(os.path.basename(x).split("_")[1]))
self.assertEqual(6, len(dump_dirs))

for i, dump_dir in enumerate(dump_dirs):
    self._assert_correct_run_subdir_naming(os.path.basename(dump_dir))
    dump = debug_data.DebugDumpDir(dump_dir)
    if i % 2 == 0:
        self.assertGreater(dump.size, 0)
        self.assertAllClose([10.0 - 0.4 * (i / 2)],
                            dump.get_tensors("v", 0, "DebugIdentity"))
        self.assertEqual(repr(self.inc_v), dump.run_fetches_info)
        self.assertEqual(repr(None), dump.run_feed_keys_info)
    else:
        self.assertEqual(0, dump.size)
        self.assertEqual(repr(self.dec_v), dump.run_fetches_info)
        self.assertEqual(repr(None), dump.run_feed_keys_info)
