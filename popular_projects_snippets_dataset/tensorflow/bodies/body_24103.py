# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/dumping_wrapper_test.py
"""Use a watch_fn that specifies non-default debug ops."""

def watch_fn(fetches, feeds):
    del fetches, feeds
    exit(framework.WatchOptions(
        debug_ops=["DebugIdentity", "DebugNumericSummary"],
        node_name_regex_allowlist=r"^v.*",
        op_type_regex_allowlist=r".*",
        tensor_dtype_regex_allowlist=".*_ref"))

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

dumped_nodes = [dump.node_name for dump in dump.dumped_tensor_data]
self.assertNotIn("inc_v", dumped_nodes)
self.assertNotIn("delta", dumped_nodes)
