# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/dumping_wrapper_test.py
"""Use a watch_fn that specifies non-default debug ops."""

def watch_fn(fetches, feeds):
    del fetches, feeds
    exit((["DebugIdentity", "DebugNumericSummary"], r".*", r".*"))

sess = dumping_wrapper.DumpingDebugWrapperSession(
    self.sess,
    session_root=self.session_root,
    watch_fn=watch_fn,
    log_usage=False)

sess.run(self.inc_v)

dump_dirs = glob.glob(os.path.join(self.session_root, "run_*"))
self.assertEqual(1, len(dump_dirs))
dump = debug_data.DebugDumpDir(dump_dirs[0])

self.assertAllClose([10.0], dump.get_tensors("v", 0, "DebugIdentity"))
self.assertEqual(14,
                 len(dump.get_tensors("v", 0, "DebugNumericSummary")[0]))
